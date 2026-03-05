import requests
from bs4 import BeautifulSoup
def task_func(url, tag):
    """
    Scrape a web page for the first occurrence of a specified HTML tag and return its text content.
    :param url: The URL of the web page to scrape.
    :param tag: The HTML tag to search for.
    :return: The text content of the specified HTML tag if found, otherwise returns None.
    """
    # Send a GET request to the URL and get the HTML response
    response = requests.get(url)
    html = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the first occurrence of the specified tag
    tag_element = soup.find(tag)

    # Return the text content of the tag if found, otherwise return None
    if tag_element is not None:
        return tag_element.text
    else:
        return None
url = 'https://www.example.com'
tag = 'h1'