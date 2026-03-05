
import binascii
import hashlib
import re

OUTPUT_DIR = './output'

def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.match(pattern, file):
                file_paths.append(os.path.join(root, file))

    hashes = {}
    for file_path in file_paths:
        with open(file_path, 'rb') as f:
            data = f.read()
            hash = hashlib.sha256(data).hexdigest()
            hashes[file_path] = hash

    return hashes