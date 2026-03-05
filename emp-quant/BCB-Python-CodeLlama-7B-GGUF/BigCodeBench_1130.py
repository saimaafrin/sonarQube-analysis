
import os
import hashlib
import json
from pathlib import Path

def task_func(directory: str) -> str:
    hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            hashes[file_path] = file_hash
    with open(os.path.join(directory, 'hashes.json'), 'w') as f:
        json.dump(hashes, f)
    return os.path.join(directory, 'hashes.json')