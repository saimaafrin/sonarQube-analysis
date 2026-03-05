
import requests
from pathlib import Path
import zipfile

# Constants
DOWNLOAD_DIR = Path("downloads")
ZIP_DIR = Path("unzipped_files")

def task_func(url, filename):
    # Ensure the download directory exists
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    # Ensure the unzip directory exists
    ZIP_DIR.mkdir(parents=True, exist_ok=True)

    # Construct the full path for the downloaded zip file
    zip_path = DOWNLOAD_DIR / filename

    try:
        # Download the zip file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Write the content to the zip file
        with zip_path.open('wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        # Extract the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(ZIP_DIR)

        # List the filenames in the unzipped directory
        filenames = [f.name for f in ZIP_DIR.iterdir() if f.is_file()]

        return ("Success", filenames)

    except requests.exceptions.RequestException as e:
        return ("Error: Network-related exception", [])

    except zipfile.BadZipFile as e:
        return ("Error: File-related exception (BadZipFile)", [])

    except Exception as e:
        return ("Error: File-related exception", [])