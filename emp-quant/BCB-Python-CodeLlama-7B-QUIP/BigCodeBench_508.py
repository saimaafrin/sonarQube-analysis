
import hashlib
import io
import os

def task_func(file_path1, file_path2):
    # Check if files exist
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        raise FileNotFoundError("File not found")

    # Open files and compute MD5 hash
    with open(file_path1, "rb") as f1:
        f1_hash = hashlib.md5(f1.read())
    with open(file_path2, "rb") as f2:
        f2_hash = hashlib.md5(f2.read())

    # Compare hashes
    if f1_hash == f2_hash:
        return True
    else:
        return False