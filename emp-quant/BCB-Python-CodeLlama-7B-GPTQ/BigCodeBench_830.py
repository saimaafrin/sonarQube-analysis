import json
import os
def task_func(filename, data):
    # Check if file exists
    if os.path.exists(filename):
        # File exists, read the content
        with open(filename, 'r') as f:
            content = f.read()
    else:
        # File does not exist, write the content
        with open(filename, 'w') as f:
            json.dump(data, f)
            content = f.read()
    # Return the content
    return content
data = {'name': 'John', 'age': 30}
filename = 'data.json'