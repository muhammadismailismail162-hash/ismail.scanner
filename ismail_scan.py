#!/usr/bin/env python3
import socket
import threading
from datetime import datetime

# Custom Branding for the tool
AUTHOR = "Muhammad Ismail"
BANNER = f"""
#################################################
#           PORT SCANNER BY {AUTHOR}        #
#           Operating on: Kali Linux            #
#################################################
"""

def scan_port(ip, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Fast scanning
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        sock.close()
    except Exception:
        pass

def start_scanner():
    print(BANNER)
    target = input("Enter website URL (e.g., google.com): ")
    
    try:
        # 1. Get the IP Address
        target_ip = socket.gethostbyname(target)
        print(f"\n[*] Target Resolved: {target_ip}")
        print(f"[*] Scan started at: {datetime.now()}\n")

        # 2. Multi-threaded Port Scanning
        # We scan the most common ports (1-1024)
        print(f"--- Scanning Ports 1-1024 ---")
        threads = []
        for port in range(1, 1025):
            t = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

        print(f"\n[*] Scan Completed by {AUTHOR}.")

    except socket.gaierror:
        print("\n[!] Error: Could not resolve hostname.")
    except KeyboardInterrupt:
        print("\n[!] Scan stopped by user.")

if __name__ == "__main__":
    start_scanner()
