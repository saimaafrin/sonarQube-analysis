
import hashlib
import io
import os

def task_func(file_path1, file_path2):
    # Check if either file exists
    if not os.path.exists(file_path1):
        raise FileNotFoundError(f"The file {file_path1} does not exist.")
    if not os.path.exists(file_path2):
        raise FileNotFoundError(f"The file {file_path2} does not exist.")
    
    # Open the files in binary mode
    with open(file_path1, 'rb') as file1, open(file_path2, 'rb') as file2:
        # Read the contents of the files
        content1 = file1.read()
        content2 = file2.read()
        
        # Compute the MD5 hash of each file
        md5_hash1 = hashlib.md5(content1).hexdigest()
        md5_hash2 = hashlib.md5(content2).hexdigest()
        
        # Compare the MD5 hashes
        return md5_hash1 == md5_hash2