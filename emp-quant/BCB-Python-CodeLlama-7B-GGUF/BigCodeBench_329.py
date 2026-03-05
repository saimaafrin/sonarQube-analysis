
import re
import json
import os

def task_func(file_path: str, regex_pattern=r'\(.+?\)|\w') -> dict:
    """
    Extracts matches from a JSON file based on a predefined regular pattern.

    Args:
        file_path (str): Path to the JSON file.
        regex_pattern (str, optional): Regular expression pattern to use for matching. Defaults to r'\(.+?\)|\w'.

    Returns:
        dict: A dictionary with the JSON file name as the key and a list of matches as values.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    matches = {}
    for filename, content in data.items():
        matches[filename] = []
        for match in re.findall(regex_pattern, content):
            matches[filename].append(match)

    return matches