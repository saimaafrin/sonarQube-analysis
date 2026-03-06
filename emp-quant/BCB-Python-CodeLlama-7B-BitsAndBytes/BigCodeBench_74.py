
import socket
import requests

def task_func(host):
    if not host:
        raise ValueError("Host cannot be None or an empty string")

    try:
        ip_address = socket.gethostbyname(host)
    except socket.gaierror:
        raise ValueError("Invalid hostname")

    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Problem connecting to the geolocation service")

    data = response.json()
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