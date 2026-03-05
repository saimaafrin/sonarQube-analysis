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
    ip_range = IPv4Network(ip_range)
    active_ips = {}
    for ip in ip_range:
        try:
            subprocess.check_output(["ping", "-c", "1", str(ip)])
            active_ips[ip] = True
        except subprocess.CalledProcessError:
            active_ips[ip] = False
    return active_ips
ip_range = "192.168.1.0/24"