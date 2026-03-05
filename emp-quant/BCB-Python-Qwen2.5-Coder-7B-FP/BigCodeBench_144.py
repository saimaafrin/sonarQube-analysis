import ipaddress
import requests
def task_func(ip_range, timeout):
    """
    Scans a specified IP address range and sends an HTTP GET request to each IP to verify if it is an active web server.
    
    Args:
    ip_range (str): The IP range in CIDR format (e.g., '192.168.0.0/16').
    timeout (int): The timeout value in seconds for the HTTP request.
    
    Returns:
    list: A list of IP addresses that responded with a status code of 200.
    
    Raises:
    ValueError: If an invalid IP range is provided.
    """
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