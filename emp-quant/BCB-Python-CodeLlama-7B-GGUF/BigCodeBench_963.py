
import os
import glob
from pathlib import Path
import zipfile

def task_func(source_directory, target_directory, zip_name):
    if not os.path.exists(source_directory):
        raise OSError("Source directory does not exist")

    # Create the target directory if it does not exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Create the zip file
    with zipfile.ZipFile(os.path.join(target_directory, zip_name + ".zip"), "w") as zip_file:
        # Iterate over the files in the source directory
        for file in glob.glob(os.path.join(source_directory, "*.txt"), glob.glob(os.path.join(source_directory, "*.docx"), glob.glob(os.path.join(source_directory, "*.xlsx"), glob.glob(os.path.join(source_directory, "*.csv")))):
            # Add the file to the zip file if it has a valid extension
            if file.suffix in [".txt", ".docx", ".xlsx", ".csv"]:
                zip_file.write(file, arcname=file.name)

    # Return the full path to the created zip file
    return os.path.join(target_directory, zip_name + ".zip")