
import re
import json
import os

def task_func(file_path: str, regex_pattern=r'\(.+?\)|\w') -> dict:
    matches_dict = {}
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        for key, value in json_data.items():
            if isinstance(value, str):
                matches = re.findall(regex_pattern, value)
                matches_dict[key] = matches
    return matches_dict