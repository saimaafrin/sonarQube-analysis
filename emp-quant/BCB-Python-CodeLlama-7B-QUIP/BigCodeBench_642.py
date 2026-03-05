
import binascii
import hashlib
import re
OUTPUT_DIR = './output'
def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    # Create a dictionary to store the file paths and their SHA256 hashes
    file_hashes = {}
    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Check if the file matches the regex pattern
        if re.match(pattern, file):
            # Open the file and read its contents
            with open(os.path.join(directory, file), 'rb') as f:
                contents = f.read()
            # Compute the SHA256 hash of the file's contents
            hash = binascii.hexlify(hashlib.sha256(contents))
            # Add the file path and its SHA256 hash to the dictionary
            file_hashes[file] = hash
    return file_hashes