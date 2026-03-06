
import re
import socket

def task_func(ip_addresses: list) -> dict:
    ip_to_hostname = {}
    for ip in ip_addresses:
        try:
            # Attempt to get the hostname from the IP address
            hostname, _, _ = socket.gethostbyaddr(ip)
            ip_to_hostname[ip] = hostname
        except socket.herror:
            # If an error occurs (e.g., unknown IP), set the hostname to None
            ip_to_hostname[ip] = None
    return ip_to_hostname