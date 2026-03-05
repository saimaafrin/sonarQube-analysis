import socket
from ipaddress import IPv4Network
from threading import Thread
def task_func(ip_range, port):
    """
    Scans a specified IP address range and checks if a specified port is open on each IP.
    The function returns a dictionary with IP addresses as keys and a boolean indicating the port's status (True if open, False otherwise).
    """
    # Create a dictionary to store the results
    results = {}

    # Iterate over the IP addresses in the range
    for ip in IPv4Network(ip_range):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the IP address and port
        try:
            sock.connect((ip, port))
        except socket.error:
            # If the connection fails, the port is not open
            results[ip] = False
        else:
            # If the connection succeeds, the port is open
            results[ip] = True

        # Close the socket
        sock.close()

    return results
ip_range = "192.168.1.0/24"
port = 80