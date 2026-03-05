
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

        if response.status_code == 200:
            content = response.text
            if use_lxml:
                parser = 'lxml'
            else:
                parser = 'html.parser'

            try:
                return BeautifulSoup(content, parser, from_encoding=from_encoding)
            except UnicodeDecodeError:
                return None

        return None

    except (requests.RequestException, UnicodeDecodeError, ValueError) as e:
        return None