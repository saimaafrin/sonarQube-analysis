import sys
import json
from datetime import datetime
PATH_TO_APPEND = '/path/to/whatever'
JSON_FILE = '/path/to/json_file.json'
def task_func(path_to_append=PATH_TO_APPEND, json_file=JSON_FILE):
    # Append the path to sys.path
    sys.path.append(path_to_append)
    
    # Get the current date and time
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Load the JSON data
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    
    # Update the JSON data with the current date and time
    json_data['last_updated'] = current_datetime
    
    # Write the updated JSON data back to the file
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)
    
    # Return the updated JSON data
    return json_data