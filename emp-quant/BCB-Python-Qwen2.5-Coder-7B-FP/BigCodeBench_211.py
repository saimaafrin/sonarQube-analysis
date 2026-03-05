import requests
import os
import zipfile
def task_func(url, destination_directory, headers=None):
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Download the zip file
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Save the zip file to a temporary location
    zip_path = os.path.join(destination_directory, 'temp.zip')
    with open(zip_path, 'wb') as f:
        f.write(response.content)

    # Extract the contents of the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)

    # Get the list of extracted files
    extracted_files = os.listdir(destination_directory)
    extracted_files = [f for f in extracted_files if os.path.isfile(os.path.join(destination_directory, f))]

    # Remove the temporary zip file
    os.remove(zip_path)

    return extracted_files