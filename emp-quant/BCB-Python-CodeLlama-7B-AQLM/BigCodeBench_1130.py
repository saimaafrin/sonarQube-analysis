import os
import hashlib
import json
from pathlib import Path
def task_func(directory: str) -> str:
    """
    Create SHA256 hashes for all files in the specified directory, including files in subdirectories, 
    and save these hashes in a JSON file named 'hashes.json' in the given directory.

    Parameters:
    - directory (str): The path to the directory containing files to be hashed.
    
    Returns:
    str: The absolute path of the JSON file ('hashes.json') containing the hashes.
    
    Requirements:
    - os
    - hashlib
    - json
    - pathlib.Path

    Example:
    >>> json_file = task_func("/path/to/directory")
    >>> print(f"Hashes saved at: {json_file}")
    """
    # Create a list of all files in the directory and subdirectories
    files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            files.append(os.path.join(root, file))

    # Create a dictionary of hashes
    hashes = {}
    for file in files:
        with open(file, "rb") as f:
            hashes[file] = hashlib.sha256(f.read()).hexdigest()

    # Save the hashes in a JSON file
    json_file = os.path.join(directory, "hashes.json")
    with open(json_file, "w") as f:
        json.dump(hashes, f)

    return json_file