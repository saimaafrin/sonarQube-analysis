import requests
from bs4 import BeautifulSoup
def task_func(url, tag):
    """
    Scrape a web page for the first occurrence of a specified HTML tag and return its text content.
    :param url: The URL of the web page to scrape.
    :param tag: The HTML tag to search for.
    :return: The text content of the specified HTML tag if found, otherwise returns None.
    """
    # Send a request to the web page and get the HTML content
    response = requests.get(url)
    html = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the first occurrence of the specified tag
    tag_found = soup.find(tag)

    # If the tag was found, return its text content
    if tag_found:
        return tag_found.text
    else:
        return None
url = 'https://www.example.com'
tag = 'h1'