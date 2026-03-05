
import json
import os
import glob

# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def task_func(directory):
    updated_files = 0
    for file in glob.glob(os.path.join(directory, '*.json')):
        with open(file, 'r') as f:
            data = json.load(f)
        if KEY not in data:
            data[KEY] = VALUE
            with open(file, 'w') as f:
                json.dump(data, f, indent=4)
            updated_files += 1
    return updated_files