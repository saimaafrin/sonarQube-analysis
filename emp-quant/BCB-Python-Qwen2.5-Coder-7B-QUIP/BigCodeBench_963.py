
import os
import glob
from pathlib import Path
import zipfile
from typing import List, Union

def task_func(source_directory: str, target_directory: str, zip_name: str) -> str:
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise OSError(f"Source directory '{source_directory}' does not exist.")

    # Define the valid extensions
    valid_extensions = ['.txt', '.docx', '.xlsx', '.csv']

    # Find all files with the valid extensions in the source directory
    files_to_zip = []
    for ext in valid_extensions:
        files_to_zip.extend(glob.glob(os.path.join(source_directory, f"*{ext}")))

    # Create the target directory if it does not exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Create the zip file
    zip_path = os.path.join(target_directory, zip_name + ".zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files_to_zip:
            zipf.write(file, os.path.basename(file))

    return zip_path