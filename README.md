# 🛡️ HTTP Brute-Force Simulator & Defensive Logging

## Overview
This project is a Python-based client-server architecture designed to simulate a dictionary attack against a local HTTP authentication endpoint. It demonstrates both offensive scripting techniques (automation, wordlist iteration) and defensive programming principles (centralized event logging, connection handling, and robust exception management).

## 🚀 Key Features
* **Automated Dictionary Attack:** Efficiently reads and processes password payloads from an external wordlist, stripping hidden characters for accurate HTTP POST requests.
* **Centralized Security Logging:** The server utilizes an isolated module (`logger.py`) to asynchronously append failed authentication attempts to a forensic `security_log.txt` file.
* **Advanced Error Handling & Resilience:**
  * **File System Protection:** Gracefully handles missing or corrupted wordlists (`FileNotFoundError`).
  * **Network Resilience:** Implements connection timeouts and catches dropped connections (`ConnectionRefusedError`, `TimeoutError`) to prevent application crashes during target downtime.
  * **Resource Management:** Strict implementation of `finally` blocks ensures TCP connections are securely closed, preventing memory leaks and orphaned sockets.
  * **Graceful Interruptions:** Safely catches `KeyboardInterrupt` (Ctrl+C) for controlled manual shutdowns.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Protocols:** HTTP, TCP
* **Core Libraries:** `http.client`, `http.server`

## ⚠️ Disclaimer
**For Educational Purposes Only.** This tool was developed to understand the mechanics of authentication vulnerabilities and defensive logging. It should only be used in authorized, local environments.