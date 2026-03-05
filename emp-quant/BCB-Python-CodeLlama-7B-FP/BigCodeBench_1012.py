import requests
from pathlib import Path
import zipfile
DOWNLOAD_DIR = Path("downloads")
ZIP_DIR = Path("unzipped_files")
def task_func(url, filename):
    """
    Downloads and extracts a zip file from a specified URL.

    Args:
        url (str): The URL of the zip file to download.
        filename (str): The name of the zip file to download.

    Returns:
        tuple: A tuple containing a status message and a list of filenames in the unzipped directory, or an empty list if extraction fails.
    """
    # Create the download directory if it doesn't exist
    if not DOWNLOAD_DIR.exists():
        DOWNLOAD_DIR.mkdir()

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