import os
import glob
from pathlib import Path
import zipfile
def task_func(source_directory, target_directory, zip_name):
    """
    Zip files with certain extensions from a source directory and save it as a zip file saved to a target directory.
    """
    if not os.path.exists(source_directory):
        raise OSError("Source directory does not exist.")

    # Create a list of files with valid extensions
    files = [f for f in glob.glob(os.path.join(source_directory, "*.txt"))
                  if f.endswith((".txt", ".docx", ".xlsx", ".csv"))]

    # Create a zip file with the files
    with zipfile.ZipFile(os.path.join(target_directory, zip_name + ".zip"), "w") as zip_file:
        for file in files:
            zip_file.write(file, os.path.basename(file))

    # Return the full path to the created zip file
    return os.path.join(target_directory, zip_name + ".zip")
source_directory = "path/to/source/directory"
target_directory = "path/to/target/directory"
zip_name = "zip_name"