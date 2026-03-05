
import urllib.request
import os
import hashlib
import tarfile
# Constants
TARGET_TAR_FILE = "downloaded_files.tar.gz"
EXPECTED_MD5_CHECKSUM = "d41d8cd98f00b204e9800998ecf8427e"

def task_func(url):
    # Download the tar.gz file
    try:
        urllib.request.urlretrieve(url, TARGET_TAR_FILE)
    except Exception as e:
        print(f"Failed to download file: {e}")
        return False

    # Calculate the MD5 checksum of the downloaded file
    with open(TARGET_TAR_FILE, 'rb') as f:
        md5_checksum = hashlib.md5(f.read()).hexdigest()

    # Check if the checksum matches the expected value
    if md5_checksum == EXPECTED_MD5_CHECKSUM:
        # Extract the contents of the tar.gz file
        with tarfile.open(TARGET_TAR_FILE, 'r:gz') as tar:
            tar.extractall(path='extracted_files')
        os.remove(TARGET_TAR_FILE)
        return True
    else:
        os.remove(TARGET_TAR_FILE)
        return False