
import requests
from bs4 import BeautifulSoup

def task_func(url, tag):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the first occurrence of the specified tag
    tag_element = soup.find(tag)

    # Return the text content of the tag if found, otherwise return None
    if tag_element:
        return tag_element.text.strip()
    else:
        return None