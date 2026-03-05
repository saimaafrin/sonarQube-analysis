import hashlib
import io
import os
def task_func(file_path1, file_path2):
    """
    Compares two files to determine if they are identical by computing and comparing their MD5 hash values.
    This method is effective for checking if two files have exactly the same content.
    """
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        raise FileNotFoundError("One or both of the files do not exist.")

    with open(file_path1, "rb") as file1, open(file_path2, "rb") as file2:
        md5_hash1 = hashlib.md5(file1.read()).hexdigest()
        md5_hash2 = hashlib.md5(file2.read()).hexdigest()

    return md5_hash1 == md5_hash2