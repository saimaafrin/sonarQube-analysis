
import binascii
import hashlib
import re
import os

OUTPUT_DIR = './output'

def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    matching_files = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if re.search(pattern, file):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    file_content = f.read()
                    sha256_hash = hashlib.sha256(file_content).hexdigest()
                    matching_files[file_path] = sha256_hash
    return matching_files