
import binascii
import hashlib
import re

OUTPUT_DIR = './output'

def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    file_paths = []
    file_hashes = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(pattern, file):
                file_paths.append(os.path.join(root, file))

    for file_path in file_paths:
        with open(file_path, 'rb') as f:
            file_hashes[file_path] = binascii.b2a_hex(hashlib.sha256(f.read()).digest())

    return file_hashes