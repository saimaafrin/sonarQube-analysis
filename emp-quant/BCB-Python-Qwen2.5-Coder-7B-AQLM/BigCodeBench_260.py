
import json
import os
import glob

# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def task_func(directory):
    updated_count = 0
    # Iterate over all JSON files in the directory
    for json_file in glob.glob(os.path.join(directory, '*.json')):
        with open(json_file, 'r+') as file:
            data = json.load(file)
            # Check if the key already exists
            if KEY not in data:
                data[KEY] = VALUE
                updated_count += 1
            # Move the file pointer to the beginning of the file
            file.seek(0)
            # Write the updated JSON data back to the file
            json.dump(data, file, indent=4)
            # Truncate the file to remove any extra data
            file.truncate()
    return updated_count