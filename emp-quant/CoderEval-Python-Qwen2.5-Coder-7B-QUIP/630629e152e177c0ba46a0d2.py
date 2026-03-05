import requests
from bs4 import BeautifulSoup

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve a and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    url = f"https://diaspora-activity.linux.org/.well-known/webfinger?resource=acct:{handle}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = {}
        for link in soup.find_all('link'):
            data[link.get('rel', '')] = link.get('href', '')
        return data
    else:
        return {}