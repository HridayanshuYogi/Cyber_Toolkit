import socket

def scan_ports(target_host, port_range=(1, 1024)):
    """
    Scans a given host over a specified range of ports using TCP connections.
    Returns a list of open ports.
    """
    open_ports = []
    
    # Try resolving host to IP if a domain name was provided
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[-] Error: Could not resolve hostname {target_host}")
        return None

    print(f"\n[*] Starting scan on target: {target_ip}")
    print(f"[*] Scanning ports {port_range[0]} through {port_range[1]}...\n")

    for port in range(port_range[0], port_range[1] + 1):
        # AF_INET = IPv4, SOCK_STREAM = TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)  # Fast timeout so it doesn't hang long on closed ports
        
        result = s.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
            print(f"[+] Port {port}: OPEN")
        
        s.close()

    return open_ports
