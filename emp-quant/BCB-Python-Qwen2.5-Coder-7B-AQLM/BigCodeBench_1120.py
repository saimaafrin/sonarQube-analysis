
import re
import urllib.parse
import requests
import json

def task_func(myString, API_KEY):
    # Regular expression to find URLs in the string
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store the geolocation data for each domain
    geolocation_data = {}
    
    for url in urls:
        # Parse the URL to extract the domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        # Construct the API request URL
        api_url = f'https://ipapi.co/{domain}/json/?access_key={API_KEY}'
        
        try:
            # Make the API request
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            # Parse the JSON response
            data = response.json()
            geolocation_data[domain] = data
        except requests.RequestException:
            # If the request fails, store None for this domain
            geolocation_data[domain] = None
    
    return geolocation_data