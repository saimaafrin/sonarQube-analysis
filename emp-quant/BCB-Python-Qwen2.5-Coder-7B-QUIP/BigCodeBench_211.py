
import requests
import os
import zipfile
def task_func(url, destination_directory, headers=None):
    # Download the zip file
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Save the zip file to a temporary location
    zip_path = os.path.join(destination_directory, 'temp.zip')
    with open(zip_path, 'wb') as f:
        f.write(response.content)

    # Extract the contents of the zip file
    extracted_files = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)
        extracted_files = zip_ref.namelist()

    # Remove the temporary zip file
    os.remove(zip_path)

    return extracted_files