import requests
from bs4 import BeautifulSoup
def task_func(url, tag):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first occurrence of the specified tag
        first_tag = soup.find(tag)
        
        # Return the text content of the tag if found, otherwise return None
        return first_tag.get_text() if first_tag else None
    except requests.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"An error occurred: {e}")
        return None
url = "https://example.com"
tag = "h1"