import binascii
import hashlib
import re
import os
def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    # Compile the regex pattern for efficiency
    regex = re.compile(pattern)
    # Dictionary to store file paths and their SHA256 hashes
    file_hashes = {}
    
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file name matches the pattern
            if regex.search(file):
                file_path = os.path.join(root, file)
                # Open the file and compute SHA256 hash
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    sha256_hash = hashlib.sha256(file_data).hexdigest()
                    file_hashes[file_path] = sha256_hash
    
    return file_hashes