import urllib.request
import os
import hashlib
import tarfile
TARGET_TAR_FILE = "downloaded_files.tar.gz"
EXPECTED_MD5_CHECKSUM = "d41d8cd98f00b204e9800998ecf8427e"
def task_func(url):
    try:
        # Download the tar.gz file
        urllib.request.urlretrieve(url, TARGET_TAR_FILE)
        
        # Calculate the MD5 checksum of the downloaded file
        with open(TARGET_TAR_FILE, 'rb') as f:
            md5_checksum = hashlib.md5(f.read()).hexdigest()
        
        # Check if the MD5 checksum matches the expected value
        if md5_checksum == EXPECTED_MD5_CHECKSUM:
            # Extract the contents of the tar.gz file
            with tarfile.open(TARGET_TAR_FILE, 'r:gz') as tar:
                tar.extractall()
            return True
        else:
            # Delete the downloaded file if the checksum does not match
            os.remove(TARGET_TAR_FILE)
            return False
    except Exception as e:
        # Handle any exceptions that may occur during the process
        print(f"An error occurred: {e}")
        if os.path.exists(TARGET_TAR_FILE):
            os.remove(TARGET_TAR_FILE)
        return False