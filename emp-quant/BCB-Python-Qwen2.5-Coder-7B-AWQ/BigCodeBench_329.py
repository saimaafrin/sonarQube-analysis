import re
import json
import os
def task_func(file_path: str, regex_pattern=r'\(.+?\)|\w') -> dict:
    # Initialize a dictionary to store the results
    results = {}
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Extract the filename from the file path
    filename = os.path.basename(file_path)
    
    # Find all matches using the provided regex pattern
    matches = re.findall(regex_pattern, json.dumps(data))
    
    # Store the matches in the dictionary
    results[filename] = matches
    
    return results