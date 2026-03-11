import socket

def check_port(host, port):
    # Create a socket object using TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout so the script doesn't hang
    s.settimeout(2)
    
    try:
        # Attempt to connect to the host and port
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        s.close()
    except Exception as e:
        print(f"Could not connect: {e}")

# Example usage (Testing your own localhost)
target_ip = "127.0.0.1" 
target_port = 80
check_port(target_ip, target_port)