
import urllib.request
import os
import zipfile

# Constants
TARGET_DIR = "downloaded_files"
TARGET_ZIP_FILE = "downloaded_files.zip"

def task_func(url):
    # Check if the target directory exists
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    # Download the zip file
    with urllib.request.urlopen(url) as response:
        with open(TARGET_ZIP_FILE, "wb") as f:
            f.write(response.read())

    # Extract the contents of the zip file
    with zipfile.ZipFile(TARGET_ZIP_FILE, "r") as zf:
        zf.extractall(TARGET_DIR)

    # Return the path of the extracted directory
    return TARGET_DIR