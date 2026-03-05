
import hashlib
import io
import os

def task_func(file_path1, file_path2):
    # Check if either file exists
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        raise FileNotFoundError("One or both of the files do not exist.")

    # Calculate MD5 hash for each file
    with open(file_path1, 'rb') as file1, open(file_path2, 'rb') as file2:
        hash1 = hashlib.md5(file1.read()).hexdigest()
        hash2 = hashlib.md5(file2.read()).hexdigest()

    # Compare the hashes
    return hash1 == hash2