
import subprocess
from ipaddress import IPv4Network

def task_func(ip_range):
    ip_range = IPv4Network(ip_range)
    ip_list = [str(ip) for ip in ip_range.hosts()]
    active_ips = {}
    for ip in ip_list:
        try:
            subprocess.check_call(["ping", "-c", "1", ip])
            active_ips[ip] = True
        except subprocess.CalledProcessError:
            active_ips[ip] = False
    return active_ips