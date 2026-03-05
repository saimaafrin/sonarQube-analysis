import urllib.request
import os
import zipfile
TARGET_DIR = "downloaded_files"
TARGET_ZIP_FILE = "downloaded_files.zip"
def task_func(url):
    # Create target directory if it does not exist
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    # Download zip file
    urllib.request.urlretrieve(url, TARGET_ZIP_FILE)

    # Extract zip file
    with zipfile.ZipFile(TARGET_ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(TARGET_DIR)

    # Delete local zip file
    os.remove(TARGET_ZIP_FILE)

    # Return path of extracted directory
    return TARGET_DIR