
import re
import socket

def task_func(ip_addresses: list) -> dict:
    hostname_dict = {}
    for ip_address in ip_addresses:
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            hostname_dict[ip_address] = hostname
        except socket.gaierror:
            hostname_dict[ip_address] = None
    return hostname_dict