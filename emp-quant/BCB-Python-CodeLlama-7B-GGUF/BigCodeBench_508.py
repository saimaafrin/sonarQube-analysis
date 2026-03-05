
import hashlib
import io
import os

def task_func(file_path1, file_path2):
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        raise FileNotFoundError("One or both of the files do not exist")

    with open(file_path1, "rb") as f1, open(file_path2, "rb") as f2:
        md5_hash1 = hashlib.md5(f1.read()).hexdigest()
        md5_hash2 = hashlib.md5(f2.read()).hexdigest()

    return md5_hash1 == md5_hash2