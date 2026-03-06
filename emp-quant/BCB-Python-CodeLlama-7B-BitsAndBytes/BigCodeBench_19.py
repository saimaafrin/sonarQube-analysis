
import os
import glob
import zipfile

def task_func(directory):
    # Check if the specified directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    # Get a list of all files in the directory
    files = glob.glob(os.path.join(directory, '*'))

    # Create a new zip file with the name 'files.zip'
    with zipfile.ZipFile('files.zip', 'w') as zip_file:
        # Add all files to the zip file
        for file in files:
            zip_file.write(file)

    # Return the path to the generated zip file
    return 'files.zip'