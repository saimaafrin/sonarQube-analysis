
import socket
from ipaddress import IPv4Network
from threading import Thread

def task_func(ip_range, port):
    # Split the IP range into network and host parts
    network, host = ip_range.split('/')
    network = IPv4Network(network)
    
    # Create a dictionary to store the results
    results = {}
    
    # Define a function to check if a port is open on a specific IP
    def check_port(ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    
    # Create a list of threads to check the ports in parallel
    threads = []
    for ip in network.hosts():
        thread = Thread(target=check_port, args=(str(ip),))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    # Populate the results dictionary with the port status
    for ip in network.hosts():
        results[str(ip)] = check_port(str(ip))
    
    return results