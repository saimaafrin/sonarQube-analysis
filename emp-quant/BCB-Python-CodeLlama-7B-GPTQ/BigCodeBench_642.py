import binascii
import hashlib
import re
def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    """
    Searches for files within the specified directory matching a given regex pattern and computes a SHA256 hash of each file's content.
    The function should output with:
        dict: A dictionary with file paths as keys and their SHA256 hashes as values.
    """
    file_hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.match(pattern, file):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    file_hashes[file_path] = binascii.hexlify(hashlib.sha256(f.read()).digest()).decode()
    return file_hashes