

import nmap

def scan_specific_services(target):
    nm = nmap.PortScanner()
    
    # Defining the specific ports:
    # 21 (FTP), 22 (SSH), 137-139 (NetBIOS), 445 (SMB)
    ports = '21,22,137,138,139,445'
    
    print(f"--- Starting targeted scan on {target} ---")
    
    # -sV: Version detection
    # -sC: Run default Nmap scripts
    nm.scan(target, ports, arguments='-sV -sC')
    
    if target not in nm.all_hosts():
        print("Target appears to be down or unreachable.")
        return

    host = nm[target]
    print(f"\nHost Status: {host.state()}")

    for proto in host.all_protocols():
        print(f"\nProtocol: {proto.upper()}")
        lport = host[proto].keys()
        
        for port in sorted(lport):
            state = host[proto][port]['state']
            service = host[proto][port]['name']
            product = host[proto][port].get('product', 'N/A')
            extrainfo = host[proto][port].get('extrainfo', '')
            
            print(f"[{port}] {service: <10} Status: {state: <8} Info: {product} {extrainfo}")
            
            # Print script output if available (useful for SMB/NetBIOS)
            if 'script' in host[proto][port]:
                for script_id, result in host[proto][port]['script'].items():
                    print(f"  |_ {script_id}: {result.strip()}")

# Usage
target_ip = "192.168.1.1" # Change this to your target
scan_specific_services(target_ip)
