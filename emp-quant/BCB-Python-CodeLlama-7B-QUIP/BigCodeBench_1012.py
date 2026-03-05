
import requests
from pathlib import Path
import zipfile

# Constants
DOWNLOAD_DIR = Path("downloads")
ZIP_DIR = Path("unzipped_files")

def task_func(url, filename):
    try:
        # Download the file
        response = requests.get(url)
        if response.status_code == 200:
            # Extract the zip file
            with zipfile.ZipFile(io.BytesIO(response.content)) as zf:
                zf.extractall(ZIP_DIR)
                filenames = [file.name for file in zf.infolist()]
                return ("Success", filenames)
        else:
            return ("Error", [])
    except Exception as e:
        return ("Error", [])