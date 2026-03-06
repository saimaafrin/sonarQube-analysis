
import requests
from pathlib import Path
import zipfile

# Constants
DOWNLOAD_DIR = Path("downloads")
ZIP_DIR = Path("unzipped_files")

def task_func(url, filename):
    # Ensure the download directory exists
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    
    # Construct the full path for the downloaded file
    download_path = DOWNLOAD_DIR / filename
    
    try:
        # Download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Save the file to disk
        with open(download_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Ensure the ZIP directory exists
        ZIP_DIR.mkdir(parents=True, exist_ok=True)
        
        # Extract the ZIP file
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(ZIP_DIR)
        
        # List the files in the extracted directory
        extracted_files = [f.name for f in ZIP_DIR.iterdir()]
        
        return ("Success", extracted_files)
    
    except requests.exceptions.RequestException as e:
        return ("Network Error: " + str(e), [])
    
    except zipfile.BadZipFile as e:
        return ("File Error: Invalid ZIP file", [])
    
    except Exception as e:
        return ("File Error: " + str(e), [])