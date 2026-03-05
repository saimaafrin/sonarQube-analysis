
import requests
import os
import zipfile

def task_func(url, destination_directory, headers=None):
    # Download the zip file
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Save the zip file to a temporary file
        with open(os.path.join(destination_directory, 'temp.zip'), 'wb') as f:
            f.write(response.content)

        # Extract the zip file
        with zipfile.ZipFile(os.path.join(destination_directory, 'temp.zip'), 'r') as zip_ref:
            zip_ref.extractall(destination_directory)

        # Get the list of extracted files
        extracted_files = [f for f in os.listdir(destination_directory) if os.path.isfile(os.path.join(destination_directory, f))]

        # Remove the temporary file
        os.remove(os.path.join(destination_directory, 'temp.zip'))

        return extracted_files
    else:
        raise Exception('Failed to download zip file')