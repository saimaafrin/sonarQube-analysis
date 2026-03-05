
import subprocess
from ipaddress import IPv4Network

def task_func(ip_range):
    active_ips = {}
    network = IPv4Network(ip_range)
    
    for ip in network.hosts():
        try:
            response = subprocess.run(['ping', '-c', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            active_ips[str(ip)] = True
        except subprocess.CalledProcessError:
            active_ips[str(ip)] = False
    
    return active_ips