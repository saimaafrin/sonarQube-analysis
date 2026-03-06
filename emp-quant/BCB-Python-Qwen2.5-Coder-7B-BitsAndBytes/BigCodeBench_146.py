
import subprocess
from ipaddress import IPv4Network

def task_func(ip_range):
    """
    Scans the specified IP address range and pings each IP to check if it is active.
    
    Args:
        ip_range (str): The IP address range in CIDR notation (e.g., '192.168.1.0/24').
    
    Returns:
        dict: A dictionary mapping IP addresses to their active status.
    """
    active_ips = {}
    network = IPv4Network(ip_range)
    
    for ip in network.hosts():
        try:
            # Ping the IP address
            response = subprocess.run(['ping', '-c', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
            if response.returncode == 0:
                active_ips[str(ip)] = True
            else:
                active_ips[str(ip)] = False
        except subprocess.CalledProcessError as e:
            print(f"Subprocess error occurred while pinging {ip}: {e}")
            active_ips[str(ip)] = False
    
    return active_ips