import urllib.request
import zipfile
import os
import urllib.error
def task_func(
    url: str,
    save_path: str = "downloaded_file.zip",
    extract_path: str = "extracted_files",
) -> str:
    """
    Downloads, extracts, and deletes a ZIP file from a specified URL.
    The function includes comprehensive error handling to manage issues such as invalid URLs, unreachable servers, corrupted ZIP files, and file I/O errors.
    In the event of a failure, it provides a descriptive error message.
    """
    try:
        # Download the ZIP file
        with urllib.request.urlopen(url) as response:
            with open(save_path, "wb") as out_file:
                out_file.write(response.read())

        # Extract the ZIP file
        with zipfile.ZipFile(save_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)

        # Delete the ZIP file
        os.remove(save_path)

        # Return the path to the extracted directory
        return extract_path

    except urllib.error.URLError as e:
        # URL Error: The URL is invalid or the server cannot be reached
        return f"URL Error: {e}"

    except zipfile.BadZipFile as e:
        # ZIP File Error: The ZIP file is corrupted or invalid
        return f"ZIP File Error: {e}"

    except FileNotFoundError as e:
        # File I/O Error: The file cannot be found or opened
        return f"File I/O Error: {e}"

    except Exception as e:
        # Unknown Error: The function failed for an unknown reason
        return f"Unknown Error: {e}"
url = "https://www.example.com/example.zip"
save_path = "downloaded_file.zip"
extract_path = "extracted_files"