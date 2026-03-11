
import nmap

def scan_target_services():
    # Initialize the scanner
    nm = nmap.PortScanner()
    
    # 1. Ask for Target
    print("--- Service Specific Scanner ---")
    target = input("Enter Target IP or Subnet (e.g., 192.168.1.1 or 192.168.1.0/24): ")
    
    # Define ports for: FTP(21), SSH(22), NetBIOS(137-139), SMB(445)
    target_ports = '21,22,137,138,139,445'
    
    print(f"\nStarting targeted scan on {target} for ports {target_ports}...")
    
    # -sV: Service version detection
    # -sC: Default Nmap scripts (very useful for SMB/NetBIOS info)
    try:
        nm.scan(hosts=target, ports=target_ports, arguments='-sV -sC')
    except Exception as e:
        print(f"Error running scan: {e}")
        return

    # 2. Process Results
    for host in nm.all_hosts():
        print(f"\nHost : {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        
        for proto in nm[host].all_protocols():
            print(f"Protocol : {proto.upper()}")
            
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                product = nm[host][proto][port].get('product', '')
                version = nm[host][proto][port].get('version', '')
                
                print(f"  [Port {port}] Status: {state} | Service: {service} ({product} {version})")
                
                # Print extra script output (e.g., SMB share names, SSH host keys)
                if 'script' in nm[host][proto][port]:
                    for script_id, output in nm[host][proto][port]['script'].items():
                        print(f"    |_ {script_id}: {output.strip()}")

if __name__ == "__main__":
    scan_target_services()
