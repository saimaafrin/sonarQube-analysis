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
    except urllib.error.URLError as e:
        return f"URL Error: {e.reason}"
    
    try:
        # Extract the ZIP file
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
    except zipfile.BadZipFile:
        os.remove(save_path)
        return "Error: Corrupted ZIP file"
    except Exception as e:
        os.remove(save_path)
        return f"Error: {e}"
    
    # Clean up the downloaded ZIP file
    os.remove(save_path)
    
    return extract_path