
import socket
from concurrent.futures import ThreadPoolExecutor

def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Fast timeout for speed
    try:
        if s.connect_ex((ip, port)) == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

def main():
    target = input("Enter target IP (e.g., 192.168.1.1): ")
    print(f"Scanning {target} from port 1 to 60000...")

    # Using ThreadPoolExecutor to run 500 checks at a time
    with ThreadPoolExecutor(max_workers=500) as executor:
        for port in range(1, 60001):
            executor.submit(check_port, target, port)

if __name__ == "__main__":
    main()
