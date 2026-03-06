
from bs4 import BeautifulSoup
import requests

# Constants
URL = "http://example.com"

def task_func(url=URL, from_encoding="cp1251", use_lxml=False):
    if not url:
        return None
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        # Decode the content using the specified encoding
        content = response.content.decode(from_encoding, errors='ignore')
        
        # Parse the HTML using BeautifulSoup
        if use_lxml:
            soup = BeautifulSoup(content, 'lxml')
        else:
            soup = BeautifulSoup(content, 'html.parser')
        
        return soup
    except (requests.RequestException, UnicodeDecodeError) as e:
        print(f"An error occurred: {e}")
        return None