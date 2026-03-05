
import os
import hashlib
import json
from pathlib import Path

def task_func(directory: str) -> str:
    # Create a dictionary to store file paths and their SHA256 hashes
    file_hashes = {}

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Calculate the SHA256 hash of the file
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            # Store the file path and its hash in the dictionary
            file_hashes[file_path] = file_hash

    # Construct the path for the output JSON file
    json_file_path = os.path.join(directory, 'hashes.json')

    # Write the dictionary to a JSON file
    with open(json_file_path, 'w') as f:
        json.dump(file_hashes, f, indent=4)

    # Return the absolute path of the JSON file
    return str(Path(json_file_path).resolve())