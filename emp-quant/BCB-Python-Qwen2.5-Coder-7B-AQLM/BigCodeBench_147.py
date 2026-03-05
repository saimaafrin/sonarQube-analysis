
import socket
from ipaddress import IPv4Network
from threading import Thread

def task_func(ip_range, port):
    results = {}
    network = IPv4Network(ip_range)
    
    def check_port(ip):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            results[ip] = result == 0
        except Exception as e:
            results[ip] = False
        finally:
            sock.close()
    
    threads = []
    for ip in network.hosts():
        thread = Thread(target=check_port, args=(str(ip),))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return results