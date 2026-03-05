
import os
import glob
from pathlib import Path
import zipfile

def task_func(source_directory, target_directory, zip_name):
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise OSError(f"The source directory {source_directory} does not exist.")
    
    # Define valid extensions
    valid_extensions = ['.txt', '.docx', '.xlsx', '.csv']
    
    # Create a list to hold the paths of files to be zipped
    files_to_zip = []
    
    # Walk through the source directory
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            # Check if the file has a valid extension
            if any(file.endswith(ext) for ext in valid_extensions):
                files_to_zip.append(os.path.join(root, file))
    
    # Create the target directory if it does not exist
    Path(target_directory).mkdir(parents=True, exist_ok=True)
    
    # Create the zip file
    zip_path = os.path.join(target_directory, f"{zip_name}.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files_to_zip:
            # Add file to the zip file
            zipf.write(file, os.path.relpath(file, source_directory))
    
    # Return the full path to the created zip file
    return zip_path