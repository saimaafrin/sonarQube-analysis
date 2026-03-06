
import os
import hashlib
import json
from pathlib import Path

def task_func(directory: str) -> str:
    # Create a dictionary to store the hashes
    hashes = {}

    # Iterate over all files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Calculate the SHA256 hash of the file
            with open(os.path.join(root, file), 'rb') as f:
                hash = hashlib.sha256(f.read()).hexdigest()

            # Add the hash to the dictionary
            hashes[file] = hash

    # Save the hashes to a JSON file
    with open(os.path.join(directory, 'hashes.json'), 'w') as f:
        json.dump(hashes, f)

    # Return the absolute path of the JSON file
    return os.path.join(directory, 'hashes.json')

# Call the function with the directory path as an argument
directory = '/path/to/directory'
result = task_func(directory)
print(result)