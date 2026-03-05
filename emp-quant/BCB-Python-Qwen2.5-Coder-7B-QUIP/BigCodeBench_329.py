
import re
import json
import os

def task_func(file_path: str, regex_pattern=r'\(.+?\)|\w') -> dict:
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Initialize the result dictionary
    result = {}

    # Open the file and read the content
    with open(file_path, 'r') as file:
        content = file.read()

        # Find all matches based on the regex pattern
        matches = re.findall(regex_pattern, content)

        # Add the matches to the result dictionary
        result[os.path.basename(file_path)] = matches

    return result