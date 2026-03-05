import os
import hashlib
import json
from pathlib import Path
def task_func(directory: str) -> str:
    # Create a dictionary to store file paths and their SHA256 hashes
    file_hashes = {}

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Open the file in binary mode and read its contents
            with open(file_path, 'rb') as f:
                file_content = f.read()
                # Calculate the SHA256 hash of the file content
                sha256_hash = hashlib.sha256(file_content).hexdigest()
                # Store the file path and its hash in the dictionary
                file_hashes[file_path] = sha256_hash

    # Convert the dictionary to a JSON string
    json_data = json.dumps(file_hashes, indent=4)

    # Construct the path for the 'hashes.json' file
    json_file_path = os.path.join(directory, 'hashes.json')

    # Write the JSON data to the 'hashes.json' file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

    # Return the absolute path of the 'hashes.json' file
    return os.path.abspath(json_file_path)