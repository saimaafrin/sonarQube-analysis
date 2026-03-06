
import re
import urllib.parse
import requests
import json

def task_func(myString, API_KEY):
    # Extract all URLs from the string
    urls = re.findall(r'https?://\S+', myString)

    # Create a dictionary to store the results
    results = {}

    # Iterate over the URLs and get the domain
    for url in urls:
        domain = urllib.parse.urlparse(url).netloc

        # Use the IP API to get the geolocation data for the domain
        response = requests.get(f'http://api.ipapi.com/v1/ip_api/{domain}/json/?key={API_KEY}')

        # Check if the API request was successful
        if response.status_code == 200:
            # Parse the JSON response and extract the relevant data
            data = json.loads(response.text)
            results[domain] = {
                'status': data['status'],
                'country': data['country'],
                'region': data['region'],
                'city': data['city'],
                'latitude': data['latitude'],
                'longitude': data['longitude']
            }
        else:
            results[domain] = None

    return results