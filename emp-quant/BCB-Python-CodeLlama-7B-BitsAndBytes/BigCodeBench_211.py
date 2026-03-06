
import requests
import os
import zipfile

def task_func(url, destination_directory, headers=None):
    # Download the zip file
    response = requests.get(url, headers=headers)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))

    # Extract the contents of the zip file to the specified directory
    zip_file.extractall(destination_directory)

    # Get the list of extracted files
    extracted_files = os.listdir(destination_directory)

    # Return the list of extracted files
    return extracted_files