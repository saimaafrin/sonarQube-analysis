
import urllib.request
import os
import zipfile

# Constants
TARGET_DIR = "downloaded_files"
TARGET_ZIP_FILE = "downloaded_files.zip"

def task_func(url):
    # Create the target directory if it does not exist
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    # Download the zip file
    with urllib.request.urlopen(url) as response:
        with open(TARGET_ZIP_FILE, "wb") as file:
            file.write(response.read())

    # Extract the zip file
    with zipfile.ZipFile(TARGET_ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(TARGET_DIR)

    # Delete the zip file
    os.remove(TARGET_ZIP_FILE)

    # Return the path of the extracted directory
    return TARGET_DIR