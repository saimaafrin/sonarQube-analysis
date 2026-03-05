
import socket
import requests

def task_func(host):
    if not host:
        raise ValueError("Host cannot be None or an empty string")

    try:
        ip_address = socket.gethostbyname(host)
    except socket.gaierror:
        raise ConnectionError("Hostname could not be resolved")

    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}")
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        raise ConnectionError("Geolocation service is not available")

    return {
        "ip_address": ip_address,
        "country": data["country"],
        "region": data["region"],
        "city": data["city"],
        "loc": data["loc"],
        "org": data["org"],
        "postal": data["postal"],
        "timezone": data["timezone"],
    }