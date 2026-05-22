# Security logging module

def log_event(message):
    """
    Appends security events to a centralized log file.
    Utilizes append mode ('a') to ensure historical forensic data is preserved.
    """
    try:
        with open("security_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")
    except Exception as e:
        print(f"[!] Logging failure: Could not write to security log. Error: {e}")
