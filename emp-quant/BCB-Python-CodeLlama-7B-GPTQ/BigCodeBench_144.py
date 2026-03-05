import ipaddress
import requests
def task_func(ip_range, timeout):
    """
    Scans a specified IP address range and sends an HTTP GET request to each IP to verify if it is an active web server.
    The function requires an IP range in CIDR format (e.g., '192.168.0.0/16') and a timeout value in seconds.
    It returns a list of IPs where the request returned a status code of 200.
    If the request is not success, then ignore and continue to the next IP address.
    """
    # Check if the IP range is valid
    try:
        ipaddress.ip_network(ip_range)
    except ValueError:
        raise ValueError("Invalid IP range")

    # Create a list to store the IPs that responded with a status code of 200
    ip_list = []

    # Iterate over the IP addresses in the range
    for ip in ipaddress.ip_network(ip_range).hosts():
        # Send an HTTP GET request to the IP
        try:
            response = requests.get(f"http://{ip}", timeout=timeout)
        except requests.exceptions.RequestException:
            # Ignore the request exception and continue to the next IP address
            continue

        # Check if the status code is 200
        if response.status_code == 200:
            # Add the IP to the list of IPs that responded with a status code of 200
            ip_list.append(ip)

    # Return the list of IPs that responded with a status code of 200
    return ip_list
ip_range = "192.168.0.0/16"
timeout = 5