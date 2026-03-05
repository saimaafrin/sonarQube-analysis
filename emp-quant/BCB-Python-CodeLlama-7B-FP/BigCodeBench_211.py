import requests
import os
import zipfile
def task_func(url, destination_directory, headers=None):
    """
    Download and extract a zip file from a URL and return a list of extracted files.

    Args:
        url (str): The URL of the zip file to download.
        destination_directory (str): The directory to extract the zip file to.
        headers (dict, optional): The headers to use when downloading the zip file.

    Returns:
        list: A list of filenames of the extracted files.
    """
    # Download the zip file
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Failed to download zip file from {url}")

    # Extract the zip file
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
        zip_file.extractall(destination_directory)

    # Get the list of extracted files
    extracted_files = os.listdir(destination_directory)

    return extracted_files
url = "https://example.com/example.zip"
destination_directory = "./extracted_files"
headers = {"Authorization": "Bearer your_token"}