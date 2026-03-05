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
    script_tags = soup.find_all('script')

    # Initialize an empty list to store the dictionaries
    dictionaries = []

    # Iterate over the <script> tags and attempt to evaluate any string within them as a Python dictionary
    for script_tag in script_tags:
        try:
            # Attempt to evaluate the string within the <script> tag as a Python dictionary
            dictionary = ast.literal_eval(script_tag.string)

            # If the evaluation was successful, add the dictionary to the list
            dictionaries.append(dictionary)
        except (ValueError, SyntaxError):
            # If the evaluation failed, ignore the <script> tag
            pass

    # Return the list of dictionaries
    return dictionaries
url = 'https://www.example.com'