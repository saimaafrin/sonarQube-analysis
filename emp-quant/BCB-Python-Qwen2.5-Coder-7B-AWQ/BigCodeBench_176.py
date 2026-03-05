import re
import socket
def task_func(ip_addresses: list) -> dict:
    hostname_dict = {}
    for ip in ip_addresses:
        try:
            # Attempt to get the hostname using socket.gethostbyaddr
            hostname, _, _ = socket.gethostbyaddr(ip)
            hostname_dict[ip] = hostname
        except socket.herror:
            # If hostname cannot be determined, set the value to None
            hostname_dict[ip] = None
    return hostname_dict