
import urllib.request
import zipfile
import os
import urllib.error

def task_func(
    url: str,
    save_path: str = "downloaded_file.zip",
    extract_path: str = "extracted_files",
) -> str:
    try:
        # Download the ZIP file
        urllib.request.urlretrieve(url, save_path)
        
        # Create the extraction directory if it doesn't exist
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)
        
        # Extract the ZIP file
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        
        # Delete the downloaded ZIP file
        os.remove(save_path)
        
        return extract_path
    
    except urllib.error.URLError as e:
        return f"URL Error: {e.reason}"
    
    except zipfile.BadZipFile:
        return "Error: Corrupted ZIP file"
    
    except PermissionError:
        return "Error: Permission denied to access the file or directory"
    
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"