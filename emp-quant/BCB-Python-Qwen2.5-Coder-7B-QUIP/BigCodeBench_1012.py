
import requests
from pathlib import Path
import zipfile
# Constants
DOWNLOAD_DIR = Path("downloads")
ZIP_DIR = Path("unzipped_files")

def task_func(url, filename):
    # Ensure the download directory exists
    DOWNLOAD_DIR.mkdir(exist_ok=True)
    # Ensure the unzipped directory exists
    ZIP_DIR.mkdir(exist_ok=True)

    # Full path for the downloaded zip file
    zip_path = DOWNLOAD_DIR / filename

    try:
        # Download the zip file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Save the zip file to disk
        with zip_path.open('wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        # Extract the zip file
        extracted_files = []
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(ZIP_DIR)
            extracted_files = zip_ref.namelist()

        # Clean up the zip file
        zip_path.unlink()

        # Return success status and list of extracted files
        return ("Success", extracted_files)

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return ("Error", f"Network error: {e}")

    except zipfile.BadZipFile as e:
        # Handle file-related errors
        return ("Error", f"File error: {e}")

    except Exception as e:
        # Handle other exceptions
        return ("Error", f"Unexpected error: {e}")