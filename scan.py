
import socket
import concurrent.futures
from datetime import datetime

# Formatting Constants
YELLOW = "\033[1;93m"
RESET = "\033[0m"

def display_banner():
    # Long, large ASCII art for "Ismail" in Yellow
    banner = f"""{YELLOW}
  _____  _____ __  __          _____ _      
 |_   _|/ ____|  \/  |   /\   |_   _| |     
   | | | (___ | \  / |  /  \    | | | |     
   | |  \___ \| |\/| | / /\ \   | | | |     
  _| |_ ____) | |  | |/ ____ \ _| |_| |____ 
 |_____|_____/|_|  |_/_/    \_\_____|______|
                                            
{RESET}"""
    print(banner)

def scan_port(target_ip, port):
    """Attempt to connect to a specific port."""
    try:
        # AF_INET = IPv4, SOCK_STREAM = TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.8) # Balance between speed and accuracy
            result = s.connect_ex((target_ip, port))
            if result == 0:
                return port
    except:
        return None
    return None

def main():
    display_banner()
    
    target = input("Enter the target website or IP: ").strip()
    
    try:
        target_ip = socket.gethostbyname(target)
        print(f"\n[!] Target Resolved: {target_ip}")
        print(f"[!] Scanning ports 1-6000...")
        print(f"[!] Started at: {datetime.now().strftime('%H:%M:%S')}")
        print("-" * 50)

        # Using 100 threads to speed up the 6000-port scan
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            # Create a list of 'tasks' for ports 1 to 6000
            futures = [executor.submit(scan_port, target_ip, port) for port in range(1, 6001)]
            
            found_any = False
            for future in concurrent.futures.as_completed(futures):
                port_result = future.result()
                if port_result:
                    print(f"[{YELLOW}OPEN{RESET}] Port: {port_result}")
                    found_any = True
            
            if not found_any:
                print("No open ports found in the 1-6000 range.")

    except socket.gaierror:
        print("\n[ERROR] Could not resolve hostname.")
    except KeyboardInterrupt:
        print("\n[!] Scan stopped by user.")

    print("-" * 50)
    print(f"[!] Scan Completed at: {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()
