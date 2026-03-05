
import json
import os

def task_func(filename, data):
    # Check if the file exists
    if os.path.exists(filename):
        # If the file exists, read it and verify the content
        with open(filename, 'r') as f:
            content = f.read()
            if content == json.dumps(data):
                return (True, content)
            else:
                return (False, content)
    else:
        # If the file does not exist, write the data to the file and return the written content
        with open(filename, 'w') as f:
            f.write(json.dumps(data))
            content = f.read()
            return (True, content)