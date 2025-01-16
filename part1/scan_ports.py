import os

def scan_ports(host, from_ip, to_ip):
    for port in range(from_ip, to_ip):
        result = os.system(f"nc -zv {host} {port} 2>/dev/null")
        if result == 0:
            print(f"Port open: {port}")
        elif port % 100 == 0:
            print(f"Scanning {port}", end="\r")

scan_ports("localhost", 50, 1000)