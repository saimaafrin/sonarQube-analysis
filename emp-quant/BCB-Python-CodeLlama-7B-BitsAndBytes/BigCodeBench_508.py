
import hashlib
import io
import os

def task_func(file_path1, file_path2):
    # Check if files exist
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        raise FileNotFoundError("File not found")

    # Open files in binary mode
    with open(file_path1, "rb") as file1, open(file_path2, "rb") as file2:
        # Read file contents into memory
        file1_data = file1.read()
        file2_data = file2.read()

        # Compute MD5 hashes
        file1_hash = hashlib.md5(file1_data).hexdigest()
        file2_hash = hashlib.md5(file2_data).hexdigest()

        # Compare hashes
        if file1_hash == file2_hash:
            return True
        else:
            return False