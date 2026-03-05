
import subprocess
from ipaddress import IPv4Network

def task_func(ip_range):
    active_ips = {}
    network = IPv4Network(ip_range, strict=False)
    
    for ip in network.hosts():
        try:
            # Ping the IP address
            response = subprocess.run(['ping', '-c', '1', str(ip)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            active_ips[str(ip)] = True
        except subprocess.CalledProcessError:
            active_ips[str(ip)] = False
    
    return active_ips