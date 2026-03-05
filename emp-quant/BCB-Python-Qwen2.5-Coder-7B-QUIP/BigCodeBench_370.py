
import os
import re
import json
import glob

def task_func(directory_path: str) -> list:
    # Check if the directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")

    # Initialize a list to store the processed file names
    processed_files = []

    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(directory_path, '*.json'))

    # Process each JSON file
    for json_file in json_files:
        # Read the content of the JSON file
        with open(json_file, 'r') as file:
            content = file.read()

        # Escape double quotes by prepending them with a double backslash
        escaped_content = re.sub(r'"', r'\"', content)

        # Write the modified content back to the file
        with open(json_file, 'w') as file:
            file.write(escaped_content)

        # Add the file name to the list of processed files
        processed_files.append(json_file)

    # Return the list of processed files
    return processed_files