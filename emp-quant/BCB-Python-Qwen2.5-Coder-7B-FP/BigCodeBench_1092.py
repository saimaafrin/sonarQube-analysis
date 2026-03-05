import ast
import requests
from bs4 import BeautifulSoup
def task_func(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        script_tags = soup.find_all('script')
        dictionaries = []
        for tag in script_tags:
            script_content = tag.string
            if script_content:
                try:
                    # Attempt to evaluate the string as a Python dictionary
                    dictionary = ast.literal_eval(script_content)
                    if isinstance(dictionary, dict):
                        dictionaries.append(dictionary)
                except (SyntaxError, ValueError):
                    # Ignore strings that cannot be evaluated as dictionaries
                    continue
        return dictionaries
    except requests.RequestException:
        # Return an empty list if there's an error in the request
        return []