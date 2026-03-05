
import ast
import requests
from bs4 import BeautifulSoup

def task_func(url):
    # Fetch the webpage content
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        # Find all <script> tags
        script_tags = soup.find_all("script")
        # Initialize an empty list to store the dictionaries
        dictionaries = []
        for script_tag in script_tags:
            # Check if the script tag contains a Python dictionary
            try:
                # Evaluate the script tag as a Python dictionary
                dictionary = ast.literal_eval(script_tag.string)
                # Add the dictionary to the list
                dictionaries.append(dictionary)
            except ValueError:
                # Ignore the script tag if it does not contain a Python dictionary
                pass
        return dictionaries
    else:
        # Return an empty list if the request was not successful
        return []