
import urllib.request
import os
import hashlib
import tarfile

# Constants
TARGET_TAR_FILE = "downloaded_files.tar.gz"
EXPECTED_MD5_CHECKSUM = "d41d8cd98f00b204e9800998ecf8427e"

def calculate_md5(file_path):
    """Calculate the MD5 checksum of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def task_func(url):
    try:
        # Download the file
        urllib.request.urlretrieve(url, TARGET_TAR_FILE)
        
        # Calculate the MD5 checksum of the downloaded file
        actual_checksum = calculate_md5(TARGET_TAR_FILE)
        
        # Check if the checksum matches the expected value
        if actual_checksum == EXPECTED_MD5_CHECKSUM:
            # Extract the contents of the tar.gz file
            with tarfile.open(TARGET_TAR_FILE, 'r:gz') as tar:
                tar.extractall(path='extracted_files')
            print("File downloaded, checksum matched, and extracted successfully.")
            return True
        else:
            print("Checksum does not match the expected value.")
            os.remove(TARGET_TAR_FILE)  # Delete the downloaded file
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        if os.path.exists(TARGET_TAR_FILE):
            os.remove(TARGET_TAR_FILE)  # Clean up the partially downloaded file
        return False