
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
                contents = f.read()
                hash = hashlib.sha256(contents).hexdigest()
                hashes[file_path] = hash
    with open('hashes.json', 'w') as f:
        json.dump(hashes, f)
    return 'hashes.json'