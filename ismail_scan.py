
import subprocess
import os

# ANSI escape codes for green color
GREEN = "\033[92m"
RESET = "\033[0m"

def print_banner():
    # Large ASCII Art for "IP SCANNER"
    banner = f"""
{GREEN}
  ___  ____    ____   ____   _      _   _  _   _  _____  ____  
 |_ _||  _ \  / ___| / ___| / \    | \ | || \ | || ____||  _ \ 
  | | | |_) | \___ \ | |    / _ \   |  \| ||  \| ||  _|  | |_) |
  | | |  __/   ___) || |___/ ___ \  | |\  || |\  || |___ |  _ < 
 |___||_|     |____/  \____/_/   \_\ |_| \_||_| \_||_____||_| \_\\
{RESET}
    """
    print(banner)

def scan_ips(target_prefix):
    print(f"[*] Scanning subnet: {target_prefix}.0/24...")
    active_ips = []

    # Loop through the typical range of 1 to 254
    for i in range(1, 255):
        ip = f"{target_prefix}.{i}"
        
        # -c 1: send 1 packet
        # -W 1: wait 1 second for response
        # Using devnull to keep the output clean
        response = subprocess.run(
            ['ping', '-c', '1', '-W', '1', ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if response.returncode == 0:
            print(f"{GREEN}[+] Host Found: {ip}{RESET}")
            active_ips.append(ip)
    
    return active_ips

if __name__ == "__main__":
    # Clear terminal for better visibility
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print_banner()
    
    # Example input: 192.168.1
    network_input = input("Enter the network prefix (e.g., 192.168.1): ")
    
    found_hosts = scan_ips(network_input)
    
    print("\n--- Scan Complete ---")
    print(f"Total active hosts found: {len(found_hosts)}")
