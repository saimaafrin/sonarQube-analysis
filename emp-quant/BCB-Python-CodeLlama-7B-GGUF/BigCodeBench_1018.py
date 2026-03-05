
from bs4 import BeautifulSoup
import requests

# Constants
URL = "http://example.com"

def task_func(url=URL, from_encoding="cp1251", use_lxml=False):
    """
    Fetches a web page from a given URL, decodes its content from a specified encoding, and returns the parsed HTML using BeautifulSoup.

    Parameters:
    url (str): The URL of the web page to fetch.
    from_encoding (str): The encoding to use for decoding the web page content.
    use_lxml (bool): Whether to use the lxml parser for improved performance.

    Returns:
    BeautifulSoup object if the fetch and parse are successful, None otherwise.
    """
    if not url:
        return None

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return None

    if response.status_code != 200:
        return None

    try:
        content = response.content.decode(from_encoding)
    except UnicodeDecodeError:
        return None

    if use_lxml:
        return BeautifulSoup(content, "lxml")
    else:
        return BeautifulSoup(content, "html.parser")