import binascii
import hashlib
import re
import os
def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    # Initialize an empty dictionary to store file paths and their SHA256 hashes
    file_hashes = {}
    
    # Compile the regex pattern for better performance
    regex = re.compile(pattern)
    
    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            
            # Check if the file name matches the given regex pattern
            if regex.search(file_path):
                # Open the file in binary mode
                with open(file_path, 'rb') as f:
                    # Read the content of the file
                    content = f.read()
                    
                    # Compute the SHA256 hash of the file content
                    sha256_hash = hashlib.sha256(content).hexdigest()
                    
                    # Store the file path and its SHA256 hash in the dictionary
                    file_hashes[file_path] = sha256_hash
    
    # Return the dictionary containing file paths and their SHA256 hashes
    return file_hashes