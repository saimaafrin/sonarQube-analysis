
import binascii
import hashlib
import re
OUTPUT_DIR = './output'

def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    import os
    import glob

    # Initialize an empty dictionary to store the results
    result = {}

    # Use glob to find all files matching the pattern in the directory
    for filename in glob.glob(os.path.join(directory, pattern)):
        # Open the file and read its content
        with open(filename, 'rb') as file:
            content = file.read()

        # Compute the SHA256 hash of the file content
        sha256_hash = hashlib.sha256(content).hexdigest()

        # Store the result in the dictionary
        result[filename] = sha256_hash

    return result