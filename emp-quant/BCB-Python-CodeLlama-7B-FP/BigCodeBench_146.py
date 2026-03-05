import subprocess
from ipaddress import IPv4Network
def task_func(ip_range):
    """
    Scans the specified IP address range and pings each IP to check if it is active.
    The function returns a dictionary with IP addresses as keys and a boolean value indicating their active status (True if the ping is successful, False otherwise).
    The function should raise the exception for: subprocess.CalledProcessError: If a ping command fails due to a subprocess error.
    The function should output with:
        dict: A dictionary mapping IP addresses to their active status.
    """
    # Create a dictionary to store the IP addresses and their active status
    ip_dict = {}

    # Iterate over the IP addresses in the range
    for ip in IPv4Network(ip_range):
        # Ping the IP address
        try:
            subprocess.check_output(["ping", "-c", "1", str(ip)])
            # If the ping is successful, set the active status to True
            ip_dict[ip] = True
        except subprocess.CalledProcessError:
            # If the ping fails, set the active status to False
            ip_dict[ip] = False

    return ip_dict
ip_range = "192.168.0.0/24"