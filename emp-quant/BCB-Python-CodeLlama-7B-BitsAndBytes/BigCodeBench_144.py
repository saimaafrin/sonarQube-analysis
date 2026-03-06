
import ipaddress
import requests

def task_func(ip_range, timeout):
    # Validate the IP range
    try:
        ipaddress.ip_network(ip_range)
    except ValueError:
        raise ValueError("Invalid IP range")

    # Create a list to store the active IPs
    active_ips = []

    # Iterate over the IP addresses in the range
    for ip in ipaddress.ip_network(ip_range).hosts():
        # Send an HTTP GET request to the IP
        try:
            response = requests.get(f"http://{ip}", timeout=timeout)
        except requests.exceptions.RequestException:
            # Ignore the request exception and continue to the next IP
            continue

        # Check if the status code is 200
        if response.status_code == 200:
            # Add the IP to the list of active IPs
            active_ips.append(ip)

    # Return the list of active IPs
    return active_ips