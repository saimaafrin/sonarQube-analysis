
import ast
import requests
from bs4 import BeautifulSoup

def task_func(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all <script> tags
        script_tags = soup.find_all('script')
        # Initialize a list to store dictionaries
        found_dicts = []
        # Iterate over each <script> tag
        for tag in script_tags:
            # Check if the content of the tag is a valid Python dictionary
            try:
                # Evaluate the content of the tag as a Python dictionary
                dict_content = ast.literal_eval(tag.text.strip())
                found_dicts.append(dict_content)
            except (SyntaxError, ValueError):
                # Ignore the tag if it's not a valid dictionary
                pass
        return found_dicts
    except requests.RequestException:
        # Return an empty list if an error occurs during the request
        return []