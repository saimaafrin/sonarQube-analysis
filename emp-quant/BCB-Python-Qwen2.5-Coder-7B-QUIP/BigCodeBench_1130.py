
import os
import hashlib
import json
from pathlib import Path

def task_func(directory: str) -> str:
    # Initialize a dictionary to store file paths and their SHA256 hashes
    file_hashes = {}

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Calculate the SHA256 hash of the file
            with open(file_path, 'rb') as f:
                file_hashes[file_path] = hashlib.sha256(f.read()).hexdigest()

    # Save the dictionary to a JSON file in the given directory
    with open(os.path.join(directory, 'hashes.json'), 'w') as f:
        json.dump(file_hashes, f, indent=4)

    # Return the absolute path of the JSON file
    return os.path.join(directory, 'hashes.json')