
import socket
import requests

def task_func(host):
    if not host:
        raise ValueError("Invalid hostname")

    try:
        ip_address = socket.gethostbyname(host)
    except socket.gaierror:
        raise ConnectionError("Could not resolve hostname")

    try:
        geolocation_data = requests.get("https://ipinfo.io/" + ip_address).json()
    except requests.exceptions.RequestException:
        raise ConnectionError("Could not connect to geolocation service")

    return {
        "ip_address": ip_address,
        "geolocation": geolocation_data
    }