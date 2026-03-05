import json
import os
import glob
KEY = 'mynewkey'
VALUE = 'mynewvalue'
def task_func(directory):
    updated_count = 0
    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(directory, '*.json'))
    for json_file in json_files:
        with open(json_file, 'r+') as file:
            data = json.load(file)
            # Check if the key already exists
            if KEY not in data:
                data[KEY] = VALUE
                # Move the file pointer to the beginning of the file
                file.seek(0)
                # Write the updated JSON data
                json.dump(data, file, indent=4)
                # Truncate the file to remove any extra data
                file.truncate()
                updated_count += 1
    return updated_count