from bs4 import BeautifulSoup
import requests
URL = "http://example.com"
def task_func(url=URL, from_encoding="cp1251", use_lxml=False):
    """
    Fetches a web page from a given URL, decodes its content from a specified encoding, and returns the parsed HTML using BeautifulSoup.
    If specified, 'lxml' is used as the parser for improved performance.
    In case of any failure (like network issues, invalid URL, or decoding errors), the function returns None.
    """
    if not url:
        return None
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        content = response.content.decode(from_encoding)
        if use_lxml:
            return BeautifulSoup(content, "lxml")
        else:
            return BeautifulSoup(content)
    except requests.exceptions.RequestException:
        return None