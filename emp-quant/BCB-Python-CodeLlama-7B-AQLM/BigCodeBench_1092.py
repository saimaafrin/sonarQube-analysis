import ast
import requests
from bs4 import BeautifulSoup
def task_func(url):
    """
    Fetches the content of a webpage specified by its URL, parses it to find <script> tags,
    and attempts to evaluate any string within these tags as a Python dictionary.

    Parameters:
    - url (str): The URL of the webpage to scrape.

    Returns:
    - list of dict: A list containing dictionaries that were successfully evaluated from string representations
      found within <script> tags on the webpage. 
    
    Note:
    - If an error occurs during the request or if no dictionaries are found/evaluable, an empty list is returned.

    Requirements:
    - ast
    - requests
    - bs4.BeautifulSoup

    Example:
    >>> task_func('https://example.com')
    [{'key': 'value'}, ...]
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script')
        dicts = []
        for script in scripts:
            if script.string is not None:
                try:
                    dicts.append(ast.literal_eval(script.string))
                except (ValueError, SyntaxError):
                    pass
        return dicts
    except (requests.exceptions.RequestException, AttributeError):
        return []