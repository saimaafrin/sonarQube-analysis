import hashlib
import io
import os
def task_func(file_path1, file_path2):
    """
    Compares two files to determine if they are identical by computing and comparing their MD5 hash values.
    
    Args:
    file_path1 (str): The path to the first file.
    file_path2 (str): The path to the second file.
    
    Returns:
    bool: True if the MD5 hashes of the files match (indicating identical content), False otherwise.
    
    Raises:
    FileNotFoundError: If either file_path1 or file_path2 does not exist.
    """
    # Check if both files exist
    if not os.path.exists(file_path1):
        raise FileNotFoundError(f"The file {file_path1} does not exist.")
    if not os.path.exists(file_path2):
        raise FileNotFoundError(f"The file {file_path2} does not exist.")
    
    # Open both files in binary mode
    with open(file_path1, 'rb') as file1, open(file_path2, 'rb') as file2:
        # Create MD5 hash objects
        md5_hash1 = hashlib.md5()
        md5_hash2 = hashlib.md5()
        
        # Read and update hash string value in blocks of 4K
        for chunk in iter(lambda: file1.read(4096), b""):
            md5_hash1.update(chunk)
        for chunk in iter(lambda: file2.read(4096), b""):
            md5_hash2.update(chunk)
        
        # Compare the MD5 hash values
        return md5_hash1.hexdigest() == md5_hash2.hexdigest()