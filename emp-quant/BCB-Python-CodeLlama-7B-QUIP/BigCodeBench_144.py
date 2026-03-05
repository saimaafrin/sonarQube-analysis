
import ipaddress
import requests

def task_func(ip_range, timeout):
    # Validate the input
    try:
        ip_range = ipaddress.ip_network(ip_range, strict=False)
    except ValueError:
        raise ValueError("Invalid IP range")

    # Initialize the list of active IPs
    active_ips = []

    # Iterate over the IP addresses in the range
    for ip in ip_range:
        # Send an HTTP GET request to the IP
        response = requests.get(f"http://{ip}/")

        # Check the status code
        if response.status_code == 200:
            # Add the IP to the list of active IPs
            active_ips.append(ip)

    return active_ips