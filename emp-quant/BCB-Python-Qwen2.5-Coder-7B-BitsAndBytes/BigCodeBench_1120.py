
import re
import urllib.parse
import requests

def task_func(myString, API_KEY):
    # Regular expression to find URLs in the string
    url_pattern = re.compile(r'https?://[^\s]+')
    
    # Find all URLs in the input string
    urls = url_pattern.findall(myString)
    
    # Dictionary to store the results
    results = {}
    
    for url in urls:
        try:
            # Parse the URL to extract the domain
            parsed_url = urllib.parse.urlparse(url)
            domain = parsed_url.netloc
            
            # Construct the API request URL
            api_url = f"https://ipapi.co/{domain}/json/"
            
            # Set up headers with the API key if required
            headers = {
                "Authorization": f"Bearer {API_KEY}"
            }
            
            # Make the API request
            response = requests.get(api_url, headers=headers)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                results[domain] = data
            else:
                results[domain] = None
        
        except Exception as e:
            print(f"Error processing URL {url}: {e}")
            results[url] = None
    
    return results