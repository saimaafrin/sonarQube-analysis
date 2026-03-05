
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
        raise Exception(f"Failed to download the file. Status code: {response.status_code}")

    # Save the zip file to a temporary location
    zip_path = os.path.join(destination_directory, 'temp.zip')
    with open(zip_path, 'wb') as f:
        f.write(response.content)

    # Extract the contents of the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)

    # Remove the temporary zip file
    os.remove(zip_path)

    # List the extracted files
    extracted_files = [f for f in os.listdir(destination_directory) if os.path.isfile(os.path.join(destination_directory, f))]
    return extracted_files