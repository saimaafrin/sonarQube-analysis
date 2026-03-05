
import subprocess
from ipaddress import IPv4Network

def task_func(ip_range):
    """
    Scans the specified IP address range and pings each IP to check if it is active.
    Returns a dictionary with IP addresses as keys and a boolean value indicating their active status (True if the ping is successful, False otherwise).
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