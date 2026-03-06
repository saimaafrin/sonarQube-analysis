
import socket
from ipaddress import IPv4Network
from threading import Thread

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set timeout for the socket connection attempt
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def scan_ip_range(ip_range, port):
    results = {}
    network = IPv4Network(ip_range)
    
    def worker(ip):
        results[ip] = check_port(str(ip), port)
    
    threads = []
    for ip in network.hosts():
        thread = Thread(target=worker, args=(ip,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return results