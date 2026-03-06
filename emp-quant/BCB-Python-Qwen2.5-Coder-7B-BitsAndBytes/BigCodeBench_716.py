
import sys
import json
from datetime import datetime

# Constants
PATH_TO_APPEND = '/path/to/whatever'
JSON_FILE = '/path/to/json_file.json'

def task_func(path_to_append=PATH_TO_APPEND, json_file=JSON_FILE):
    # Append the path to sys.path
    if path_to_append not in sys.path:
        sys.path.append(path_to_append)
    
    # Update the JSON file with the current date and time
    try:
        with open(json_file, 'r') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        json_data = {}
    
    json_data['last_updated'] = datetime.now().isoformat()
    
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)
    
    return json_data