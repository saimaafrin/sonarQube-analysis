
import subprocess
from ipaddress import IPv4Network

def task_func(ip_range):
    active_ips = {}
    network = IPv4Network(ip_range)
    for ip in network.hosts():
        try:
            # Ping the IP address
            result = subprocess.run(['ping', '-c', '1', str(ip)], capture_output=True, check=True)
            # If the ping is successful, the IP is active
            active_ips[str(ip)] = True
        except subprocess.CalledProcessError:
            # If the ping fails, the IP is not active
            active_ips[str(ip)] = False
    return active_ips