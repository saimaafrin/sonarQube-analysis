import requests
from xml.etree import ElementTree as ET

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve a and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    url = f"https://{handle.split('@')[1]}/.well-known/webfinger?resource=acct:{handle}"
    response = requests.get(url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        data = {}
        for link in root.findall('{http://www.w3.org/2005/Atom}link'):
            rel = link.get('rel')
            href = link.get('href')
            if rel and href:
                data[rel] = href
        return data
    else:
        raise Exception(f"Failed to retrieve webfinger document for {handle}")