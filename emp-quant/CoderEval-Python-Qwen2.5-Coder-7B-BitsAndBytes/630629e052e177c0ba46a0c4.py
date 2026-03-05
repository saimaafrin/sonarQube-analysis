import json
from typing import Dict

def parse_diaspora_webfinger(document: str) -> Dict:
    data = json.loads(document)
    hcard_url = next((link['href'] for link in data.get('links', []) if link.get('rel') == 'hcard'), None)
    return {'hcard_url': hcard_url}