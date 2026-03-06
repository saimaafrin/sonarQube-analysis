
import json
import os
import glob

# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def task_func(directory):
    updated_count = 0
    for file in glob.glob(os.path.join(directory, '*.json')):
        with open(file, 'r+') as f:
            data = json.load(f)
            if KEY not in data:
                data[KEY] = VALUE
                updated_count += 1
                f.seek(0)
                json.dump(data, f, indent=4)
    return updated_count