
import hashlib
import io
import os

def task_func(file_path1, file_path2):
    # Check if both files exist
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        raise FileNotFoundError("One or both of the files do not exist.")

    # Function to compute MD5 hash of a file
    def compute_md5(file_path):
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buf = f.read(65536)
            while buf:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()

    # Compute MD5 hash for both files
    md5_file1 = compute_md5(file_path1)
    md5_file2 = compute_md5(file_path2)

    # Compare the MD5 hashes
    return md5_file1 == md5_file2