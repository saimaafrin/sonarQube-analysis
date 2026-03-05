import ast
import requests
from bs4 import BeautifulSoup
def task_func(url):
    """
    Fetches the content of a webpage specified by its URL, parses it to find <script> tags, and attempts to evaluate any string within these tags as a Python dictionary.
    Note that: If an error occurs during the request or if no dictionaries are found/evaluable, an empty list is returned.
    The function should output with:
        list of dict: A list containing dictionaries that were successfully evaluated from string representations
        found within <script> tags on the webpage.
    """
    # Fetch the webpage content
    response = requests.get(url)
    if response.status_code != 200:
        return []

    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <script> tags
    scripts = soup.find_all('script')

    # Initialize an empty list to store the dictionaries
    dictionaries = []

    # Iterate over the <script> tags and attempt to evaluate their contents as Python dictionaries
    for script in scripts:
        try:
            # Evaluate the script contents as a Python dictionary
            dictionary = ast.literal_eval(script.string)

            # Add the dictionary to the list if it is not empty
            if dictionary:
                dictionaries.append(dictionary)
        except (ValueError, SyntaxError):
            # Ignore any errors and continue
            pass

    return dictionaries
url = 'https://www.example.com'