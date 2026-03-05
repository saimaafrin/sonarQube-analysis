import binascii
import hashlib
import re
import os
def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    matching_files = {}
    # Compile the regex pattern for efficiency
    regex = re.compile(pattern)
    
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Check if the file name matches the pattern
            if regex.search(file_path):
                # Compute SHA256 hash of the file content
                with open(file_path, 'rb') as f:
                    file_content = f.read()
                    sha256_hash = hashlib.sha256(file_content).hexdigest()
                    matching_files[file_path] = sha256_hash
    
    return matching_files