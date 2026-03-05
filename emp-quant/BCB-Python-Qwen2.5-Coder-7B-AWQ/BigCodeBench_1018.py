from bs4 import BeautifulSoup
import requests
URL = "http://example.com"
def task_func(url=URL, from_encoding="cp1251", use_lxml=False):
    if not url:
        return None

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        if response.status_code == 200:
            content = response.content.decode(from_encoding, errors='ignore')
            if use_lxml:
                return BeautifulSoup(content, 'lxml')
            else:
                return BeautifulSoup(content, 'html.parser')
        else:
            return None
    except (requests.RequestException, UnicodeDecodeError):
        return None