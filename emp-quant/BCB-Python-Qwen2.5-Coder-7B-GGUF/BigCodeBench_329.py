
import re
import json
import os

def task_func(file_path: str, regex_pattern=r'\(.+?\)|\w') -> dict:
    """
    Extracts matches from a JSON file based on a predefined regular pattern.
    
    Args:
    file_path (str): The path to the JSON file.
    regex_pattern (str): The regular expression pattern to use for matching. Defaults to r'\(.+?\)|\w'.
    
    Returns:
    dict: A dictionary with the JSON file name as the key and a list of matches as values.
    """
    # Extract the filename from the file path
    filename = os.path.basename(file_path)
    
    # Initialize an empty list to store matches
    matches = []
    
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Convert the JSON data to a string
    json_string = json.dumps(data)
    
    # Find all matches using the regular expression pattern
    matches = re.findall(regex_pattern, json_string)
    
    # Return a dictionary with the filename as the key and the list of matches as the value
    return {filename: matches}