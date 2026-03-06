
import requests
import os
import zipfile

def task_func(url, destination_directory, headers=None):
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Download the zip file
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to download file: {response.status_code}")

    # Save the zip file to disk
    zip_path = os.path.join(destination_directory, "temp.zip")
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