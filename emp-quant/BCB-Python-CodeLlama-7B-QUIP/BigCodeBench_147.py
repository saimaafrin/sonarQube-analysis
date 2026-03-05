
import socket
from ipaddress import IPv4Network
from threading import Thread

def task_func(ip_range, port):
    # Create a list of IP addresses in the specified range
    ip_list = [str(ip) for ip in IPv4Network(ip_range).hosts()]

    # Create a dictionary to store the port status for each IP address
    port_status = {}

    # Iterate over the IP addresses and check if the specified port is open
    for ip in ip_list:
        try:
            # Create a socket and connect to the specified port on the current IP address
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            # If the connection is successful, the port is open
            port_status[ip] = True
        except socket.error:
            # If the connection is unsuccessful, the port is not open
            port_status[ip] = False

    # Return the dictionary with the port status for each IP address
    return port_status

# Create a list of IP addresses in the specified range
ip_list = [str(ip) for ip in IPv4Network("192.168.1.0/24").hosts()]

# Create a dictionary to store the port status for each IP address
port_status = {}

# Iterate over the IP addresses and check if the specified port is open
for ip in ip_list:
    # Create a socket and connect to the specified port on the current IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 80))
    # If the connection is successful, the port is open
    port_status[ip] = True

# Return the dictionary with the port status for each IP address
return port_status