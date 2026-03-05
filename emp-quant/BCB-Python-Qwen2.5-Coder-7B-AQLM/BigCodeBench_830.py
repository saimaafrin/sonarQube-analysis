
import json
import os

def task_func(filename, data):
    try:
        # Write the dictionary to a file as a JSON object
        with open(filename, 'w') as file:
            json.dump(data, file)
        
        # Check if the file exists
        if os.path.exists(filename):
            # Read the content back to verify
            with open(filename, 'r') as file:
                written_data = json.load(file)
            
            # Return a tuple with success status and written data
            return (True, written_data)
        else:
            return (False, None)
    except Exception as e:
        return (False, None)