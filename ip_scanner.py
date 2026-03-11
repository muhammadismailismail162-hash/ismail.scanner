
import socket

def display_banner():
    # ANSI Color Codes
    GREEN = "\033[92m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # Large stylized banner for "Ismail_scanner"
    banner = f"""
{GREEN}{BOLD}
  _____                      _ _                                                        
 |_   _|                    (_) |                                                       
   | |  ___ _ __ ___   __ _ _| |     ___  ___ __ _ _ __  _ __   ___ _ __ 
   | | / __| '_ ` _ \ / _` | | |    / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
  _| |_\__ \ | | | | | (_| | | |    \__ \ (_| (_| | | | | | | |  __/ |   
 |_____|___/_| |_| |_|\__,_|_|_|    |___/\___\__,_|_| |_|_| |_|\___|_|   
                                                                         
{RESET}
    """
    print(banner)

def get_target_ip():
    display_banner()
    
    target = input("Enter the target URL or Domain: ").strip()
    
    # Removing http/https if the user accidentally includes it
    if target.startswith(("http://", "https://")):
        target = target.split("//")[-1].split("/")[0]

    try:
        print(f"\n[+] Scanning target: {target}")
        ip_address = socket.gethostbyname(target)
        print(f"[+] IP Address Found: \033[94m{ip_address}\033[0m")
    except socket.gaierror:
        print(f"[-] Error: Unable to resolve host '{target}'. Check the name or your connection.")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_target_ip()
