
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
        
        # Parse the JSON response
        geolocation_info = response.json()
        
        # Return the IP address and geolocation information
        return {
            'ip_address': ip_address,
            'geolocation': geolocation_info
        }
    
    except socket.gaierror:
        raise ConnectionError("Failed to resolve the IP address of the host")
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to fetch geolocation information: {e}")