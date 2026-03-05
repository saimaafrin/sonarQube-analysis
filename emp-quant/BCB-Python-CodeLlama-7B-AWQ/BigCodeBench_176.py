import re
import socket
def task_func(ip_addresses: list) -> dict:
    """
    Given a list of IP addresses, this function returns a dictionary mapping each valid IP address to its respective hostname. If the hostname cannot be determined, the value will be None.
    """
    hostname_dict = {}
    for ip_address in ip_addresses:
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            hostname_dict[ip_address] = hostname
        except socket.herror:
            hostname_dict[ip_address] = None
    return hostname_dict
ip_addresses = ['192.168.1.1', '192.168.1.2', '192.168.1.3']