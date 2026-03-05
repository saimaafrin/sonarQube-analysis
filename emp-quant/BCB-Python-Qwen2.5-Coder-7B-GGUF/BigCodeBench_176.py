
import re
import socket

def task_func(ip_addresses: list) -> dict:
    hostname_dict = {}
    for ip in ip_addresses:
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            hostname_dict[ip] = hostname
        except socket.herror:
            hostname_dict[ip] = None
    return hostname_dict