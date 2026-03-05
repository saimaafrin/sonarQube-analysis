import subprocess
from ipaddress import IPv4Network
def task_func(ip_range):
    active_ips = {}
    network = IPv4Network(ip_range)
    
    for ip in network.hosts():
        try:
            # Ping the IP and check the return code
            response = subprocess.run(['ping', '-c', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if response.returncode == 0:
                active_ips[str(ip)] = True
            else:
                active_ips[str(ip)] = False
        except subprocess.CalledProcessError as e:
            # Raise the exception if ping command fails
            raise e
    
    return active_ips