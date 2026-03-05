import ipaddress
import requests
def task_func(ip_range, timeout):
    """
    Scans a specified IP address range and sends an HTTP GET request to each IP to verify if it is an active web server.
    The function requires an IP range in CIDR format (e.g., '192.168.0.0/16') and a timeout value in seconds.
    It returns a list of IPs where the request returned a status code of 200. If the request is not success, then ignore and continue to the next IP address.
    The function should raise the exception for:
        ValueError: If an invalid IP range is provided.
    The function should output with:
        list: A list of IP addresses that responded with a status code of 200.
    """
    try:
        # Validate the IP range
        ip_range = ipaddress.ip_network(ip_range)
    except ValueError:
        raise ValueError("Invalid IP range provided")

    # Create a list to store the active IPs
    active_ips = []

    # Iterate over the IPs in the range
    for ip in ip_range:
        # Send an HTTP GET request to the IP
        try:
            response = requests.get(f"http://{ip}", timeout=timeout)
        except requests.exceptions.Timeout:
            # If the request times out, ignore and continue to the next IP
            continue
        except requests.exceptions.ConnectionError:
            # If the request fails, ignore and continue to the next IP
            continue

        # Check if the request returned a status code of 200
        if response.status_code == 200:
            # If the request was successful, add the IP to the list of active IPs
            active_ips.append(ip)

    # Return the list of active IPs
    return active_ips
ip_range = "192.168.0.0/16"
timeout = 5