import json
import os
import glob
KEY = 'mynewkey'
VALUE = 'mynewvalue'
def task_func(directory):
    # Initialize variables
    updated_files = 0
    # Iterate over all JSON files in the directory
    for file in glob.glob(os.path.join(directory, '*.json')):
        # Open the JSON file
        with open(file, 'r') as f:
            data = json.load(f)
        # Check if the key already exists
        if KEY not in data:
            # Add the new key-value pair
            data[KEY] = VALUE
            # Update the JSON file
            with open(file, 'w') as f:
                json.dump(data, f, indent=4)
            # Increment the number of updated files
            updated_files += 1
    # Return the number of updated files
    return updated_files
directory = 'path/to/directory'