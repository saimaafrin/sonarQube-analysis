
import os
import hashlib
import json
from pathlib import Path

def task_func(directory: str) -> str:
    # Create a dictionary to store file paths and their corresponding SHA256 hashes
    file_hashes = {}
    
    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Open the file in binary mode and read its contents
            with open(file_path, 'rb') as f:
                file_data = f.read()
                # Calculate the SHA256 hash of the file content
                sha256_hash = hashlib.sha256(file_data).hexdigest()
                # Store the file path and its hash in the dictionary
                file_hashes[file_path] = sha256_hash
    
    # Define the path for the output JSON file
    json_file_path = Path(directory) / 'hashes.json'
    
    # Write the dictionary to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(file_hashes, json_file, indent=4)
    
    # Return the absolute path of the JSON file
    return str(json_file_path.resolve())