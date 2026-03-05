
import json
from glob import glob

def task_func(directory, string):
    matching_files = []
    # Recursively find all JSON files in the directory and its subdirectories
    json_files = glob(directory + '/**/*.json', recursive=True)
    
    for json_file in json_files:
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
                # Recursively search for the string in the JSON data structure
                if search_in_json(data, string):
                    matching_files.append(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Handle cases where the file is not found or is not a valid JSON file
            continue
    
    return matching_files

def search_in_json(data, string):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == string or search_in_json(value, string):
                return True
    elif isinstance(data, list):
        for item in data:
            if search_in_json(item, string):
                return True
    elif isinstance(data, str) and data == string:
        return True
    return False