
import json
import os
import glob
# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'
def task_func(directory):
    # Get all JSON files in the directory
    files = glob.glob(directory + '/*.json')
    # Initialize the number of updated files
    num_updated = 0
    # Loop through each file
    for file in files:
        # Open the file in read mode
        with open(file, 'r') as f:
            # Load the JSON data
            data = json.load(f)
            # Check if the key already exists
            if KEY not in data:
                # Add the new key-value pair
                data[KEY] = VALUE
                # Update the file
                with open(file, 'w') as f:
                    json.dump(data, f)
                    num_updated += 1
    # Return the number of updated files
    return num_updated