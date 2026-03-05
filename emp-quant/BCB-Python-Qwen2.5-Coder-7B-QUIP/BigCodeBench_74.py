
import socket
import requests

def task_func(host):
    if not host:
        raise ValueError("Host cannot be None or an empty string")
    
    try:
        # Resolve the IP address of the given host
        ip_address = socket.gethostbyname(host)
        
        # Fetch geolocation information from the ipinfo.io API
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the response and return the IP address and geolocation information
        geolocation_info = response.json()
        geolocation_info['ip'] = ip_address
        return geolocation_info
    
    except socket.gaierror:
        raise ValueError(f"Invalid hostname: {host}")
    
    except requests.ConnectionError:
        raise ConnectionError("Failed to connect to the geolocation service")
    
    except requests.RequestException as e:
        raise ConnectionError(f"An error occurred: {e}")