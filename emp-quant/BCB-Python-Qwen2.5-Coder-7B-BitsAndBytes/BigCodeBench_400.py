
import json
from glob import glob

def task_func(directory, string):
    matching_files = []
    
    # Recursively find all JSON files in the directory and its subdirectories
    json_files = glob(f"{directory}/**/*.json", recursive=True)
    
    for json_file in json_files:
        try:
            # Open and load the JSON file
            with open(json_file, 'r') as file:
                data = json.load(file)
                
                # Check if the string is in the JSON data
                if contains_string(data, string):
                    matching_files.append(json_file)
        except Exception as e:
            print(f"Error processing {json_file}: {e}")
    
    return matching_files

def contains_string(data, string):
    if isinstance(data, dict):
        for key, value in data.items():
            if contains_string(value, string):
                return True
    elif isinstance(data, list):
        for item in data:
            if contains_string(item, string):
                return True
    elif data == string:
        return True
    
    return False