
import urllib.request
import zipfile
import os
import urllib.error

def task_func(url: str, save_path: str = "downloaded_file.zip", extract_path: str = "extracted_files") -> str:
    """
    Downloads, extracts, and deletes a ZIP file from a specified URL.

    Parameters:
    url (str): The URL of the ZIP file to download.
    save_path (str, optional): The path to save the downloaded ZIP file. Defaults to "downloaded_file.zip".
    extract_path (str, optional): The path to extract the ZIP file's contents. Defaults to "extracted_files".

    Returns:
    str: The path to the directory where the ZIP file's contents have been extracted. Returns an error message in case of failure.
    """
    try:
        # Download the ZIP file
        with urllib.request.urlopen(url) as response:
            with open(save_path, "wb") as file:
                file.write(response.read())

        # Extract the ZIP file's contents
        with zipfile.ZipFile(save_path, "r") as zip_file:
            zip_file.extractall(extract_path)

        # Delete the ZIP file
        os.remove(save_path)

        # Return the path to the extracted directory
        return extract_path

    except urllib.error.URLError as e:
        # Return an error message if the URL is invalid or the server cannot be reached
        return f"URL Error: {e}"

    except zipfile.BadZipFile as e:
        # Return an error message if the ZIP file is corrupted
        return f"Bad ZIP File: {e}"

    except FileNotFoundError as e:
        # Return an error message if the file cannot be found
        return f"File Not Found: {e}"

    except Exception as e:
        # Return an error message if any other error occurs
        return f"Unknown Error: {e}"