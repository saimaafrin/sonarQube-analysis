
import sys
import json
from datetime import datetime

# Constants
PATH_TO_APPEND = '/path/to/whatever'
JSON_FILE = '/path/to/json_file.json'

def task_func(path_to_append=PATH_TO_APPEND, json_file=JSON_FILE):
    # Add the path to sys.path
    sys.path.append(path_to_append)

    # Open the JSON file
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Update the 'last_updated' key with the current date and time
    json_data['last_updated'] = datetime.now().isoformat()

    # Write the updated JSON data back to the file
    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=4)

    return json_data

# Call the function
task_func()