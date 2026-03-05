import ipaddress
import requests
def task_func(ip_range, timeout):
    active_servers = []
    try:
        # Create an IP network object from the CIDR notation
        network = ipaddress.ip_network(ip_range)
    except ValueError:
        raise ValueError("Invalid IP range provided")

    # Iterate over all IP addresses in the network
    for ip in network.hosts():
        try:
            # Send an HTTP GET request to the current IP
            response = requests.get(f"http://{ip}", timeout=timeout)
            # Check if the response status code is 200
            if response.status_code == 200:
                active_servers.append(str(ip))
        except requests.RequestException:
            # Ignore any exceptions and continue to the next IP
            continue

    return active_servers