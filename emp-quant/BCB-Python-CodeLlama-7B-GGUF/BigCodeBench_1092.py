
import ast
import requests
from bs4 import BeautifulSoup

def task_func(url):
    # Fetch the content of the webpage
    response = requests.get(url)
    if response.status_code != 200:
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <script> tags
    scripts = soup.find_all('script')

    # Initialize an empty list to store the dictionaries
    dictionaries = []

    # Iterate over the <script> tags and attempt to evaluate the string content as a Python dictionary
    for script in scripts:
        try:
            dictionary = ast.literal_eval(script.string)
            dictionaries.append(dictionary)
        except (ValueError, SyntaxError):
            continue

    return dictionaries