
import json
import os

def task_func(filename, data):
    try:
        # Write the dictionary to a file as a JSON object
        with open(filename, 'w') as file:
            json.dump(data, file)
        
        # Check if the file exists
        if not os.path.exists(filename):
            return False, None
        
        # Read the content back from the file
        with open(filename, 'r') as file:
            read_data = json.load(file)
        
        # Verify the content
        if data == read_data:
            return True, data
        else:
            return False, data
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False, None