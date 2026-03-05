import json
from glob import glob
def task_func(directory, string):
    matching_files = []
    # Use glob to find all JSON files in the directory and its subdirectories
    json_files = glob(f"{directory}/**/*.json", recursive=True)
    
    for json_file in json_files:
        try:
            # Open and load the JSON file
            with open(json_file, 'r') as file:
                data = json.load(file)
                
                # Recursively search for the string in the JSON data
                def search_in_json(data):
                    if isinstance(data, dict):
                        for key, value in data.items():
                            if key == string or search_in_json(value):
                                return True
                    elif isinstance(data, list):
                        for item in data:
                            if search_in_json(item):
                                return True
                    return False
                
                if search_in_json(data):
                    matching_files.append(json_file)
        except json.JSONDecodeError:
            # Skip files that are not valid JSON
            continue
    
    return matching_files