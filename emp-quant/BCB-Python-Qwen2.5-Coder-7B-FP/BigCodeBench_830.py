import json
import os
def task_func(filename, data):
    try:
        # Write the dictionary to a file as a JSON object
        with open(filename, 'w') as file:
            json.dump(data, file)
        
        # Check if the file exists
        if not os.path.exists(filename):
            return (False, None, None)
        
        # Read the content back to verify
        with open(filename, 'r') as file:
            written_data = json.load(file)
        
        # Return success status and the written data
        return (True, True, written_data)
    
    except Exception as e:
        # Return failure status and None for written data
        return (False, False, None)