
import socket
import concurrent.futures
from datetime import datetime

# Formatting Constants
YELLOW = "\033[1;93m"
GREEN = "\033[1;92m"
RED = "\033[91m"
RESET = "\033[0m"

def scan_port(target_ip, port):
    """Checks a single port and returns its status."""
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # 1 second timeout for accuracy
        
        # connect_ex returns 0 for success (Open)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            return f"Port {port}: {GREEN}OPEN{RESET}"
        elif result == 11 or result == 10060: # Timeout codes
            return f"Port {port}: {YELLOW}FILTERED{RESET}"
        else:
            # Uncomment the line below if you want to see closed ports
            # return f"Port {port}: CLOSED"
            return None
        s.close()
    except:
        return None

def main():
    # The requested yellow branding
    print("-" * 50)
    print(f"Initializing Scanner: {YELLOW}Ismail{RESET}")
    print("-" * 50)

    target = input("Enter target website or IP: ").strip()
    
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Scanning Target: {target} ({target_ip})")
        print(f"Time started: {datetime.now()}")
        print("-" * 50)

        # Using ThreadPoolExecutor to scan ports 1-6000 simultaneously
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            # Map the scan_port function across the range of ports
            futures = [executor.submit(scan_port, target_ip, port) for port in range(1, 6001)]
            
            for future in concurrent.futures.as_completed(futures):
                res = future.result()
                if res: # Only print if the port was Open or Filtered
                    print(res)

    except socket.gaierror:
        print(f"{RED}Error: Hostname could not be resolved.{RESET}")
    except KeyboardInterrupt:
        print(f"\n{RED}Scan halted by user.{RESET}")

    print("-" * 50)
    print("Scan Complete.")

if __name__ == "__main__":
    main()
