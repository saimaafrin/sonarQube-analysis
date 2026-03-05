import json
import os
import glob
KEY = 'mynewkey'
VALUE = 'mynewvalue'
def task_func(directory):
    """
    Add a new key-value pair to all JSON files in a specific directory and save the updated JSON files.
    """
    updated_files = 0
    for file in glob.glob(os.path.join(directory, '*.json')):
        with open(file, 'r') as f:
            data = json.load(f)
        if KEY not in data:
            data[KEY] = VALUE
            with open(file, 'w') as f:
                json.dump(data, f)
            updated_files += 1
    return updated_files