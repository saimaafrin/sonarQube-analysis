
import os
import glob
from pathlib import Path
import zipfile

def task_func(source_directory, target_directory, zip_name):
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise OSError("Source directory does not exist")

    # Create the target directory if it does not exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Create the zip file
    zip_file = zipfile.ZipFile(os.path.join(target_directory, zip_name + ".zip"), "w")

    # Add the files to the zip file
    for file in glob.glob(os.path.join(source_directory, "*.txt")):
        zip_file.write(file, os.path.basename(file))
    for file in glob.glob(os.path.join(source_directory, "*.docx")):
        zip_file.write(file, os.path.basename(file))
    for file in glob.glob(os.path.join(source_directory, "*.xlsx")):
        zip_file.write(file, os.path.basename(file))
    for file in glob.glob(os.path.join(source_directory, "*.csv")):
        zip_file.write(file, os.path.basename(file))

    # Close the zip file
    zip_file.close()

    # Return the full path to the created zip file
    return os.path.join(target_directory, zip_name + ".zip")