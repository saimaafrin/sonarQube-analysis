import hashlib
import io
import os
def task_func(file_path1, file_path2):
    """
    Compares two files to determine if they are identical by computing and comparing their MD5 hash values.
    This method is effective for checking if two files have exactly the same content.
    """
    # Check if either file_path1 or file_path2 does not exist
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        raise FileNotFoundError("One of the files does not exist")

    # Open the files in binary mode
    with open(file_path1, "rb") as file1, open(file_path2, "rb") as file2:
        # Compute the MD5 hash of each file
        hash1 = hashlib.md5(file1.read()).hexdigest()
        hash2 = hashlib.md5(file2.read()).hexdigest()

    # Compare the MD5 hashes
    if hash1 == hash2:
        return True
    else:
        return False