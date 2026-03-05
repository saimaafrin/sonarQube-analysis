import sys
import json
from datetime import datetime
PATH_TO_APPEND = '/path/to/whatever'
JSON_FILE = '/path/to/json_file.json'
def task_func(path_to_append=PATH_TO_APPEND, json_file=JSON_FILE):
    # Append the given path to sys.path
    sys.path.append(path_to_append)

    # Open the JSON file and read its contents
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Update the 'last_updated' key in the JSON data
    json_data['last_updated'] = datetime.now().isoformat()

    # Write the updated JSON data back to the file
    with open(json_file, 'w') as f:
        json.dump(json_data, f)

    # Return the updated JSON data
    return json_data