import ast
import requests
from bs4 import BeautifulSoup
def task_func(url):
    """
    Fetches the content of a webpage specified by its URL, parses it to find <script> tags,
    and attempts to evaluate any string within these tags as a Python dictionary.
    
    Args:
    url (str): The URL of the webpage to fetch and parse.
    
    Returns:
    list of dict: A list containing dictionaries that were successfully evaluated from string representations
    found within <script> tags on the webpage.
    """
    # Initialize an empty list to store the dictionaries
    result_dicts = []
    
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <script> tags in the parsed HTML
        script_tags = soup.find_all('script')
        
        # Iterate through each <script> tag
        for script in script_tags:
            # Extract the text content of the <script> tag
            script_text = script.string
            
            # Check if the text contains a dictionary-like structure
            if script_text and '{' in script_text and '}' in script_text:
                try:
                    # Attempt to evaluate the string as a Python dictionary
                    dictionary = ast.literal_eval(script_text)
                    # Check if the evaluated object is indeed a dictionary
                    if isinstance(dictionary, dict):
                        result_dicts.append(dictionary)
                except (SyntaxError, ValueError):
                    # Ignore any errors that occur during evaluation
                    continue
    except requests.RequestException:
        # Handle any errors that occur during the request
        pass
    
    # Return the list of successfully evaluated dictionaries
    return result_dicts