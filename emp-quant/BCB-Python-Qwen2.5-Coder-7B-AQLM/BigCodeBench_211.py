
import requests
import os
import zipfile

def task_func(url, destination_directory, headers=None):
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Download the zip file
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for HTTP errors

    # Define the path to save the zip file
    zip_path = os.path.join(destination_directory, 'downloaded.zip')

    # Save the zip file to the destination directory
    with open(zip_path, 'wb') as zip_file:
        zip_file.write(response.content)

    # Extract the contents of the zip file
    extracted_files = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)
        extracted_files = zip_ref.namelist()

    # Remove the zip file after extraction
    os.remove(zip_path)

    return extracted_files