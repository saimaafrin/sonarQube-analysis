
import re
import urllib.parse
import requests
import json

def task_func(myString, API_KEY):
    # Extract all URLs from the string
    urls = re.findall(r'https?://\S+', myString)

    # Create a dictionary to store the geolocation data for each domain
    domain_geoloc_data = {}

    # Iterate over each URL and extract the domain
    for url in urls:
        domain = urllib.parse.urlparse(url).netloc

        # Use the IP API to get the geolocation data for the domain
        api_url = f'http://api.ipstack.com/{domain}?access_key={API_KEY}'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            domain_geoloc_data[domain] = data
        else:
            domain_geoloc_data[domain] = None

    return domain_geoloc_data