
import requests
from bs4 import BeautifulSoup

def task_func(url, tag):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first occurrence of the specified tag
        first_tag = soup.find(tag)

        # Return the text content of the tag if found, otherwise None
        return first_tag.text.strip() if first_tag else None
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None