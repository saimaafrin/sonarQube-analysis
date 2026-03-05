import re
import socket
def task_func(ip_addresses: list) -> dict:
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    hostname_dict = {}
    
    for ip in ip_addresses:
        if ip_pattern.match(ip):
            try:
                hostname, _, _ = socket.gethostbyaddr(ip)
                hostname_dict[ip] = hostname
            except socket.herror:
                hostname_dict[ip] = None
        else:
            hostname_dict[ip] = None
    
    return hostname_dict