
import json
import os
import glob

# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def task_func(directory):
    # Initialize counter for updated files
    updated_files_count = 0
    
    # Use glob to find all JSON files in the specified directory
    json_files = glob.glob(os.path.join(directory, '*.json'))
    
    # Iterate over each JSON file
    for file_path in json_files:
        try:
            # Open the JSON file for reading
            with open(file_path, 'r') as file:
                data = json.load(file)
            
            # Check if the key already exists
            if KEY not in data:
                # Add the new key-value pair
                data[KEY] = VALUE
            
            # Open the JSON file for writing and update the content
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            
            # Increment the counter for updated files
            updated_files_count += 1
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    return updated_files_count