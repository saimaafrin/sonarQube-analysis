
import json
import os

def task_func(filename, data):
    # Check if file exists
    if os.path.exists(filename):
        # File exists, return False
        return False

    # Write data to file as JSON object
    with open(filename, 'w') as f:
        json.dump(data, f)

    # Read data from file
    with open(filename, 'r') as f:
        read_data = json.load(f)

    # Verify content
    if read_data == data:
        # Content matches, return True
        return True, read_data
    else:
        # Content does not match, return False
        return False, read_data

if result[0]:
    print('Data written successfully')
else:
    print('Data not written successfully')

print(result[1])