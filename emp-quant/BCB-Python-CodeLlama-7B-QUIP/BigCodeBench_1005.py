
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
        with urllib.request.urlopen(url) as response:
            data = response.read()
            with open(save_path, "wb") as f:
                f.write(data)

        # Extract the ZIP file
        with zipfile.ZipFile(save_path, "r") as zf:
            zf.extractall(extract_path)

        # Delete the ZIP file
        os.remove(save_path)

        return extract_path
    except urllib.error.URLError as e:
        return "URL Error: " + str(e)
    except zipfile.BadZipFile:
        return "Corrupted ZIP file"
    except OSError as e:
        return "File I/O error: " + str(e)