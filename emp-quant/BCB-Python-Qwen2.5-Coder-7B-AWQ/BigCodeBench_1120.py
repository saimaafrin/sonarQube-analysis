import re
import urllib.parse
import requests
import json
def task_func(myString, API_KEY):
    # Regular expression to extract URLs from the string
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store the results
    results = {}
    
    # Loop through each URL
    for url in urls:
        # Parse the URL to get the domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        # Construct the API request URL
        api_url = f'https://ipapi.co/{domain}/json/?access_key={API_KEY}'
        
        try:
            # Send the request to the IP API
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            # Parse the JSON response
            data = response.json()
            
            # Store the data in the results dictionary
            results[domain] = data
        except requests.RequestException as e:
            # Handle any errors that occur during the request
            print(f'Error fetching geolocation data for {domain}: {e}')
            results[domain] = None
    
    return results