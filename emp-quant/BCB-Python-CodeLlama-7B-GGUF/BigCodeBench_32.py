
import requests
from bs4 import BeautifulSoup

def task_func(url, tag):
    """
    Scrape a web page for the first occurrence of a specified HTML tag and return its text content.

    Args:
        url (str): The URL of the web page to scrape.
        tag (str): The HTML tag to search for.

    Returns:
        str: The text content of the specified HTML tag if found, otherwise returns None.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tag_content = soup.find(tag)
    if tag_content:
        return tag_content.text.strip()
    else:
        return None