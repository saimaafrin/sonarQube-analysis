
import json
import os
import glob
# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def task_func(directory):
    updated_count = 0
    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(directory, '*.json'))
    for json_file in json_files:
        with open(json_file, 'r+') as file:
            # Load the JSON data
            data = json.load(file)
            # Check if the key exists and update if not
            if KEY not in data:
                data[KEY] = VALUE
                updated_count += 1
            # Move to the beginning of the file to overwrite
            file.seek(0)
            # Write the updated data
            json.dump(data, file, indent=4)
            # Truncate the file to remove any extra content
            file.truncate()
    return updated_count