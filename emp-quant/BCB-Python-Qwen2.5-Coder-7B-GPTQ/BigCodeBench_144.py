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
    # Validate the IP range
    try:
        network = ipaddress.ip_network(ip_range)
    except ValueError:
        raise ValueError("Invalid IP range provided")
    
    active_servers = []
    
    # Iterate over the IP addresses in the network
    for ip in network.hosts():
        try:
            # Send an HTTP GET request
            response = requests.get(f"http://{ip}", timeout=timeout)
            # Check if the response status code is 200
            if response.status_code == 200:
                active_servers.append(str(ip))
        except requests.RequestException:
            # Ignore any exceptions and continue to the next IP
            continue
    
    return active_servers