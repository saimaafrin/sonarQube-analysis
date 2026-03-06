import subprocess
from ipaddress import IPv4Network
def task_func(ip_range):
    """
    Scans the specified IP address range and pings each IP to check if it is active.
    The function returns a dictionary with IP addresses as keys and a boolean value indicating
    their active status (True if the ping is successful, False otherwise).

    Parameters:
        ip_range (str): The IP range to scan, in CIDR notation (e.g., '192.168.0.0/24').

    Requirements:
    - ipaddress
    - subprocess

    Returns:
        dict: A dictionary mapping IP addresses to their active status.

    Raises:
        subprocess.CalledProcessError: If a ping command fails due to a subprocess error.

    Examples:
    >>> result = task_func('192.168.1.0/24')
    >>> isinstance(result, dict)
    True
    >>> all(isinstance(key, str) and isinstance(value, bool) for key, value in result.items())
    True
    """
    # Convert the IP range to a network object
    ip_range = IPv4Network(ip_range)

    # Create a dictionary to store the results
    results = {}

    # Iterate over the IP addresses in the range
    for ip in ip_range:
        # Ping the IP address
        try:
            subprocess.check_output(['ping', '-c', '1', str(ip)])
        except subprocess.CalledProcessError:
            # If the ping fails, set the result to False
            results[str(ip)] = False
        else:
            # If the ping succeeds, set the result to True
            results[str(ip)] = True

    # Return the results
    return results