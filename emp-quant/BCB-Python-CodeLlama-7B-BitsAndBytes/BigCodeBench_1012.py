
import requests
from pathlib import Path
import zipfile

# Constants
DOWNLOAD_DIR = Path("downloads")
ZIP_DIR = Path("unzipped_files")

def task_func(url, filename):
    # Download the zip file
    try:
        response = requests.get(url, allow_redirects=True)
        open(DOWNLOAD_DIR / filename, "wb").write(response.content)
    except requests.exceptions.RequestException as e:
        return ("Error", [])

    # Extract the zip file
    try:
        with zipfile.ZipFile(DOWNLOAD_DIR / filename, "r") as zip_ref:
            zip_ref.extractall(ZIP_DIR)
        return ("Success", [file.name for file in ZIP_DIR.iterdir()])
    except zipfile.BadZipFile as e:
        return ("Error", [])