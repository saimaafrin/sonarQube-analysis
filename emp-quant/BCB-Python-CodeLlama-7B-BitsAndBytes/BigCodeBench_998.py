
import urllib.request
import os
import hashlib
import tarfile

# Constants
TARGET_TAR_FILE = "downloaded_files.tar.gz"
EXPECTED_MD5_CHECKSUM = "d41d8cd98f00b204e9800998ecf8427e"

def task_func(url):
    # Download the tar.gz file
    with urllib.request.urlopen(url) as response:
        with open(TARGET_TAR_FILE, "wb") as f:
            f.write(response.read())

    # Calculate the MD5 checksum of the downloaded file
    with open(TARGET_TAR_FILE, "rb") as f:
        md5_hash = hashlib.md5(f.read()).hexdigest()

    # Compare the MD5 checksum with the expected value
    if md5_hash == EXPECTED_MD5_CHECKSUM:
        # Extract the contents of the tar.gz file
        with tarfile.open(TARGET_TAR_FILE, "r:gz") as tar:
            tar.extractall()
        return True
    else:
        # Delete the downloaded file if the MD5 checksum does not match
        os.remove(TARGET_TAR_FILE)
        return False