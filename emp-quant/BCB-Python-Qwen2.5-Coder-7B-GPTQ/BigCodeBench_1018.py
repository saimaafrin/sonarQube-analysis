from bs4 import BeautifulSoup
import requests
URL = "http://example.com"
def task_func(url=URL, from_encoding="cp1251", use_lxml=False):
    if not url:
        return None

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        if use_lxml:
            soup = BeautifulSoup(response.content, 'lxml', from_encoding=from_encoding)
        else:
            soup = BeautifulSoup(response.content, 'html.parser', from_encoding=from_encoding)

        return soup
    except (requests.RequestException, ValueError, UnicodeDecodeError):
        return None