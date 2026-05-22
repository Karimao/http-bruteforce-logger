from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import logger

# Server configuration
HOST = "localhost"
PORT = 8080
SECRET_PASSWORD = "hemligt123"

class SecurityRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Validate endpoint path to prevent unauthorized directory access
        if self.path != "/login":
            self.send_error(HTTPStatus.NOT_FOUND, "Invalid Endpoint")
            return
        
        # Extract and decode the payload from the request body
        content_length = int(self.headers.get('Content-Length', 0))
        payload = self.rfile.read(content_length).decode('utf-8')

        # Authentication logic
        if payload == SECRET_PASSWORD:
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(b"Authentication Successful")
        else:
            # Trigger defensive logging mechanism upon failed attempt
            logger.log_event(f"Failed authentication attempt with payload: {payload}")
            self.send_error(HTTPStatus.UNAUTHORIZED, "Authentication Failed")

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), SecurityRequestHandler)
    print(f"[*] Target server listening on http://{HOST}:{PORT}...")
    
    try:
        # Keep the server active to listen for incoming requests
        server.serve_forever()
    except KeyboardInterrupt:
        # Graceful shutdown upon manual interrupt
        print("\n[*] Shutting down server.")
        server.server_close()
