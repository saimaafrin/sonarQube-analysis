
import requests
from bs4 import BeautifulSoup

def task_func(url, tag):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        first_tag = soup.find(tag)
        if first_tag:
            return first_tag.get_text(strip=True)
        else:
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None