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
    try:
        # Download the zip file
        response = requests.get(url, allow_redirects=True)
        open(DOWNLOAD_DIR / filename, "wb").write(response.content)

        # Extract the zip file
        with zipfile.ZipFile(DOWNLOAD_DIR / filename, "r") as zip_ref:
            zip_ref.extractall(ZIP_DIR)

        # Return a tuple containing the status message and the list of filenames in the unzipped directory
        return ("Success", [file.name for file in ZIP_DIR.iterdir()])
    except requests.exceptions.RequestException as e:
        # Return a tuple containing the status message and an empty list if the download fails
        return ("Error", [])
    except zipfile.BadZipFile as e:
        # Return a tuple containing the status message and an empty list if the extraction fails
        return ("Error", [])