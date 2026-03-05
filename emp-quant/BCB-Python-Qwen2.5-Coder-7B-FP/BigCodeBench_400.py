import json
from glob import glob
def task_func(directory, string):
    matching_files = []
    # Use glob to find all JSON files in the directory and its subdirectories
    json_files = glob(directory + '/**/*.json', recursive=True)
    
    for json_file in json_files:
        with open(json_file, 'r') as file:
            try:
                # Load the JSON data from the file
                data = json.load(file)
                # Recursively search for the string in the JSON data
                if search_in_json(data, string):
                    matching_files.append(json_file)
            except json.JSONDecodeError:
                # Skip files that are not valid JSON
                continue
    
    return matching_files
def search_in_json(data, string):
    # Check if the current data is a dictionary
    if isinstance(data, dict):
        # Check each key-value pair in the dictionary
        for key, value in data.items():
            if key == string or search_in_json(value, string):
                return True
    # Check if the current data is a list
    elif isinstance(data, list):
        # Check each item in the list
        for item in data:
            if search_in_json(item, string):
                return True
    # Check if the current data is the string we are looking for
    elif data == string:
        return True
    
    return False