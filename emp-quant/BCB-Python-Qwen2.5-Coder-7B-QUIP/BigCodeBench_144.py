
import ipaddress
import requests

def task_func(ip_range, timeout):
    # Validate the IP range
    try:
        network = ipaddress.ip_network(ip_range)
    except ValueError as e:
        raise ValueError(f"Invalid IP range: {e}")

    # Initialize a list to store active IPs
    active_ips = []

    # Iterate over the IP addresses in the network
    for ip in network.hosts():
        try:
            response = requests.get(f"http://{ip}", timeout=timeout)
            if response.status_code == 200:
                active_ips.append(ip)
        except (requests.RequestException, requests.Timeout):
            # Ignore any exceptions and continue with the next IP
            pass

    return active_ips