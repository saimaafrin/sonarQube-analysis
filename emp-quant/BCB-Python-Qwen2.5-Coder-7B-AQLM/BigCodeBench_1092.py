
import ast
import requests
from bs4 import BeautifulSoup

def task_func(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        script_tags = soup.find_all('script')
        dictionaries = []
        
        for tag in script_tags:
            content = tag.string
            if content:
                try:
                    # Attempt to evaluate the content as a Python dictionary
                    dictionary = ast.literal_eval(content)
                    if isinstance(dictionary, dict):
                        dictionaries.append(dictionary)
                except (ValueError, SyntaxError):
                    # Ignore if the content is not a valid dictionary
                    pass
        
        return dictionaries
    except requests.RequestException:
        # Return an empty list if there is an error during the request
        return []