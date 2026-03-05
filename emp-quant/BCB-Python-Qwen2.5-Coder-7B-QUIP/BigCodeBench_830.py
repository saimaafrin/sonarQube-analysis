
import json
import os

def task_func(filename, data):
    # Check if the file exists
    file_exists = os.path.exists(filename)
    
    # Write the dictionary to a file as a JSON object
    with open(filename, 'w') as file:
        json.dump(data, file)
    
    # Read the content back from the file
    with open(filename, 'r') as file:
        written_data = json.load(file)
    
    # Return a tuple with a boolean indicating success, the written data, and the file existence
    return (file_exists, written_data, file_exists)