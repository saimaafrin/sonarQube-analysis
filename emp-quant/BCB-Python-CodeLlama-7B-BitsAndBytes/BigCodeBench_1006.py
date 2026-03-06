
import os
import requests
from zipfile import ZipFile, BadZipFile

def task_func(url, download_path="mnt/data/downloads/"):
    try:
        # Download the ZIP file
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Network issue: Unable to download the file from the provided URL.")
        with open(download_path + "temp.zip", "wb") as f:
            f.write(response.content)

        # Extract the ZIP file
        with ZipFile(download_path + "temp.zip", "r") as zip_ref:
            zip_ref.extractall(download_path)

        # Remove the temporary ZIP file
        os.remove(download_path + "temp.zip")

        # Return the path to the extracted directory
        return download_path

    except BadZipFile:
        raise Exception("The downloaded file is not a valid ZIP file.")
    except Exception as e:
        raise Exception("Error: " + str(e))