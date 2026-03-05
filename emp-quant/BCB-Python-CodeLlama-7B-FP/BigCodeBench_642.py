import binascii
import hashlib
import re
def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    """
    Searches for files within the specified directory matching a given regex pattern and computes a SHA256 hash of each file's content.
    :param directory: The directory to search for files.
    :param pattern: The regex pattern to match against file names.
    :return: A dictionary with file paths as keys and their SHA256 hashes as values.
    """
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.match(pattern, file):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    hashes = {}
    for file_path in file_paths:
        with open(file_path, 'rb') as f:
            data = f.read()
            hash = hashlib.sha256(data).hexdigest()
            hashes[file_path] = hash

    return hashes