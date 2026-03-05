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
        md5_hash = hashlib.md5()
        with open(TARGET_TAR_FILE, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        
        # Compare the calculated MD5 checksum with the expected value
        if md5_hash.hexdigest() == EXPECTED_MD5_CHECKSUM:
            # Extract the contents of the tar.gz file
            with tarfile.open(TARGET_TAR_FILE, "r:gz") as tar:
                tar.extractall(path="extracted_files")
            return True
        else:
            # Delete the downloaded file if the checksum does not match
            os.remove(TARGET_TAR_FILE)
            return False
    except Exception as e:
        # Handle any exceptions that may occur during the process
        print(f"An error occurred: {e}")
        return False
url = "http://example.com/path/to/downloaded_files.tar.gz"