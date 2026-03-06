
from bs4 import BeautifulSoup
import requests

# Constants
URL = "http://example.com"

def task_func(url=URL, from_encoding="cp1251", use_lxml=False):
    # Check if the URL is valid
    if not url:
        return None

    # Send a GET request to the URL
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return None

    # Check if the HTTP response status code is 200 (OK)
    if response.status_code != 200:
        return None

    # Decode the response content using the specified encoding
    try:
        content = response.content.decode(from_encoding)
    except UnicodeDecodeError:
        return None

    # Parse the decoded content using BeautifulSoup
    try:
        soup = BeautifulSoup(content, "html.parser")
    except Exception:
        return None

    # Return the parsed HTML
    return soup