
import requests
from bs4 import BeautifulSoup

def task_func(url, tag):
    # Get the HTML content of the web page
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
    else:
        return None

    # Find the specified tag
    tag_text = soup.find(tag)

    # Return the text content of the tag if found, otherwise return None
    if tag_text:
        return tag_text.text
    else:
        return None