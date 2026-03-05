
import re
import urllib.parse
import requests
import json

def task_func(myString, API_KEY):
    # Extract URLs from the input string
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),?\\(\\),\\#\\|\\{\\}\\[\\]\\\\t\\\\n\\\\r\\x0B\\x0C\\x0D\\x0A])+(?:/[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),\\(\\),\\#\\|\\{\\}\\[\\]\\\\t\\\\n\\\\r\\x0B\\x0C\\x0D\\x0A])*', myString)
    
    # Initialize a dictionary to store the results
    results = {}
    
    # Loop through each URL and extract the domain
    for url in urls:
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        # Construct the API request URL
        api_url = f'https://ipapi.co/{domain}/json?key={API_KEY}'
        
        # Make the API request
        response = requests.get(api_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            results[domain] = response.json()
        else:
            results[domain] = None
    
    return results