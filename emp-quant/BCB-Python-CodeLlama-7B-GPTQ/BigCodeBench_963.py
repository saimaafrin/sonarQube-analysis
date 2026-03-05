import os
import glob
from pathlib import Path
import zipfile
def task_func(source_directory, target_directory, zip_name):
    """
    Zip files with certain extensions from a source directory and save it as a zip file saved to a target directory.
    """
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise OSError("Source directory does not exist")

    # Create a list of files with valid extensions
    files = []
    for ext in ['.txt', '.docx', '.xlsx', '.csv']:
        files.extend(glob.glob(os.path.join(source_directory, f"*{ext}")))

    # Create the zip file
    zip_file = zipfile.ZipFile(os.path.join(target_directory, f"{zip_name}.zip"), "w")

    # Add files to the zip file
    for file in files:
        zip_file.write(file, os.path.basename(file))

    # Close the zip file
    zip_file.close()

    # Return the full path to the created zip file
    return os.path.join(target_directory, f"{zip_name}.zip")
source_directory = "path/to/source/directory"
target_directory = "path/to/target/directory"
zip_name = "zip_file"