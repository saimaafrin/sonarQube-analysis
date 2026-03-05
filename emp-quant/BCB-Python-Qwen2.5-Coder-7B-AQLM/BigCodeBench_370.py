
import os
import re
import json
import glob

def task_func(directory_path: str) -> list:
    processed_files = []
    
    # Check if the directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory {directory_path} does not exist.")
    
    # Iterate over all JSON files in the directory
    for json_file in glob.glob(os.path.join(directory_path, '*.json')):
        try:
            # Read the content of the JSON file
            with open(json_file, 'r') as file:
                content = file.read()
            
            # Escape double quotes by prepending them with a double backslash
            escaped_content = re.sub(r'"', r'\\"', content)
            
            # Write the modified content back to the JSON file
            with open(json_file, 'w') as file:
                file.write(escaped_content)
            
            # Add the processed file to the list
            processed_files.append(json_file)
        except Exception as e:
            print(f"Error processing {json_file}: {e}")
    
    return processed_files