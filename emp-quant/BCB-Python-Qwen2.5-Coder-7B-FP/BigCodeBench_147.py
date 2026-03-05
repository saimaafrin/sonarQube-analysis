import socket
from ipaddress import IPv4Network
from threading import Thread
def task_func(ip_range, port):
    def check_port(ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0

    ip_network = IPv4Network(ip_range)
    results = {}

    def worker(ip):
        results[ip] = check_port(ip, port)

    threads = []
    for ip in ip_network.hosts():
        thread = Thread(target=worker, args=(str(ip),))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results