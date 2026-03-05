import re
import urllib.parse
import requests
import json
def task_func(myString, API_KEY):
    # Regular expression to extract URLs from the string
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store the geolocation data for each domain
    geolocation_data = {}
    
    for url in urls:
        # Parse the URL to extract the domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        # Construct the API request URL
        api_url = f'https://ipapi.co/{domain}/json/?key={API_KEY}'
        
        try:
            # Make the API request to get geolocation data
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            
            # Store the geolocation data in the dictionary
            geolocation_data[domain] = data
        except requests.RequestException as e:
            # Handle exceptions (e.g., network problems, invalid API key)
            geolocation_data[domain] = None
    
    return geolocation_data