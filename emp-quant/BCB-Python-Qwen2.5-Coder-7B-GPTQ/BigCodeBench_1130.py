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
            # Open the file in binary mode and calculate the SHA256 hash
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            # Store the file path and its hash in the dictionary
            file_hashes[file_path] = file_hash
    
    # Convert the dictionary to a JSON string
    json_data = json.dumps(file_hashes, indent=4)
    
    # Create a Path object for the output file
    output_file = Path(directory) / 'hashes.json'
    
    # Write the JSON data to the output file
    with open(output_file, 'w') as f:
        f.write(json_data)
    
    # Return the absolute path of the output file
    return str(output_file.resolve())