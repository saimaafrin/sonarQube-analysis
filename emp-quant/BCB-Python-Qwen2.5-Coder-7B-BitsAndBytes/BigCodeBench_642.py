
import binascii
import hashlib
import re
from os import listdir
from os.path import isfile, join

OUTPUT_DIR = './output'

def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    matching_files = {}
    # List all files in the directory
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    
    # Filter files based on the regex pattern
    for file in files:
        if re.search(pattern, file):
            file_path = join(directory, file)
            with open(file_path, 'rb') as f:
                file_content = f.read()
                sha256_hash = hashlib.sha256(file_content).hexdigest()
                matching_files[file_path] = sha256_hash
    
    return matching_files