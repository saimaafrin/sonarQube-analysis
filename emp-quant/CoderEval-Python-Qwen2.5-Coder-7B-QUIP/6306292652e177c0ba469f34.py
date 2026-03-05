import requests
from typing import Optional

def fetch_content_type(url: str) -> Optional[str]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.head(url, headers=headers)
    if response.status_code == 200:
        return response.headers.get('Content-Type')
    return None