import json
from typing import Dict

def parse_diaspora_webfinger(document: str) -> Dict:
    data = json.loads(document)
    hcard_url = data['hcard_url']
    links = data['links']
    hcard_url_value = [link['href'] for link in links if link['rel'] == hcard_url]
    return hcard_url_value