import re
import urllib.parse
import requests
import json
def task_func(myString, API_KEY):
    # Regular expression to extract URLs from the string
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store the results
    results = {}
    
    for url in urls:
        # Parse the URL to get the domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        # Construct the API request URL
        api_url = f'https://ipapi.co/{domain}/json/?access_key={API_KEY}'
        
        try:
            # Send the request to the IP API
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            
            # Parse the JSON response
            data = response.json()
            
            # Store the result in the dictionary
            results[domain] = data
        except requests.RequestException as e:
            # Handle any request exceptions
            print(f"Error fetching geolocation data for {domain}: {e}")
            results[domain] = None
    
    return results