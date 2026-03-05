
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
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return ("Error", [])

    # Extract the zip file
    try:
        with zipfile.ZipFile(DOWNLOAD_DIR / filename, "r") as zip_ref:
            zip_ref.extractall(ZIP_DIR)
        filenames = [f for f in ZIP_DIR.iterdir() if f.is_file()]
        return ("Success", filenames)
    except zipfile.BadZipFile:
        return ("Error", [])
    except FileNotFoundError:
        return ("Error", [])
    except Exception as e:
        return ("Error", [])