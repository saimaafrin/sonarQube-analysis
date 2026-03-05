import socket
import requests
def task_func(host):
    if not host:
        raise ValueError("Host cannot be None or an empty string")
    
    try:
        ip_address = socket.gethostbyname(host)
    except socket.gaierror:
        raise ConnectionError("Failed to resolve the IP address of the host")
    
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}")
        response.raise_for_status()
        geolocation_info = response.json()
        geolocation_info['ip'] = ip_address
        return geolocation_info
    except requests.RequestException as e:
        raise ConnectionError("Failed to fetch geolocation information") from e