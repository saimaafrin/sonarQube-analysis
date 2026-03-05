import requests
import os
import zipfile
def task_func(url, destination_directory, headers=None):
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Define the path for the downloaded zip file
    zip_file_path = os.path.join(destination_directory, 'downloaded_file.zip')

    # Save the content of the response to a zip file
    with open(zip_file_path, 'wb') as file:
        file.write(response.content)

    # Create a list to store the names of the extracted files
    extracted_files = []

    # Extract the contents of the zip file to the specified directory
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)
        # Add the names of the extracted files to the list
        extracted_files = zip_ref.namelist()

    # Remove the zip file after extraction
    os.remove(zip_file_path)

    # Return the list of extracted files
    return extracted_files