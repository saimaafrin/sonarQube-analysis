import requests
from xml.etree import ElementTree as ET

def retrieve_and_parse_diaspora_webfinger(handle):
    """
    Retrieve a and parse a remote Diaspora webfinger document.

    :arg handle: Remote handle to retrieve
    :returns: dict
    """
    url = f"https://{handle}/.well-known/webfinger"
    response = requests.get(url)
    response.raise_for_status()
    xml_data = response.text
    root = ET.fromstring(xml_data)
    result = {}
    for link in root.findall(".//{http://www.w3.org/2005/Atom}link"):
        rel = link.get("rel")
        href = link.get("href")
        if rel and href:
            result[rel] = href
    return result