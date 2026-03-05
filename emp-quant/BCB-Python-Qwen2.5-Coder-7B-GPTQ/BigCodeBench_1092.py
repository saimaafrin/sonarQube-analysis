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

        # Find all <script> tags in the HTML
        script_tags = soup.find_all('script')

        # List to store the dictionaries
        dictionaries = []

        # Iterate over each <script> tag
        for tag in script_tags:
            # Extract the content of the <script> tag
            script_content = tag.string

            # Check if the content is a valid Python dictionary string
            if script_content and script_content.strip().startswith('{') and script_content.strip().endswith('}'):
                try:
                    # Attempt to evaluate the string as a Python dictionary
                    dictionary = ast.literal_eval(script_content)
                    dictionaries.append(dictionary)
                except (SyntaxError, ValueError):
                    # If evaluation fails, skip this tag
                    continue

        return dictionaries

    except requests.RequestException:
        # If there is an error during the request, return an empty list
        return []