
import ipaddress
import requests

def task_func(ip_range, timeout):
    active_ips = []
    network = ipaddress.ip_network(ip_range, strict=False)
    
    for ip in network.hosts():
        try:
            response = requests.get(f"http://{ip}", timeout=timeout)
            if response.status_code == 200:
                active_ips.append(str(ip))
        except (requests.RequestException, ValueError):
            continue
    
    return active_ips