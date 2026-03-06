
import ast
import requests
from bs4 import BeautifulSoup

def task_func(url):
    # Fetch the webpage content
    response = requests.get(url)
    if response.status_code != 200:
        return []

    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <script> tags on the webpage
    script_tags = soup.find_all('script')

    # Initialize an empty list to store the dictionaries
    dictionaries = []

    # Iterate over the <script> tags and attempt to evaluate the string contents as Python dictionaries
    for script_tag in script_tags:
        try:
            # Use the ast module to parse the string contents of the <script> tag
            script_str = script_tag.string
            script_dict = ast.literal_eval(script_str)

            # Add the evaluated dictionary to the list of dictionaries
            dictionaries.append(script_dict)
        except (ValueError, SyntaxError):
            # If an error occurs, skip to the next <script> tag
            continue

    return dictionaries