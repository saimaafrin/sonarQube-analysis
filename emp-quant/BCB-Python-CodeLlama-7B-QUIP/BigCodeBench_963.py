
import os
import glob
from pathlib import Path
import zipfile

def task_func(source_directory, target_directory, zip_name):
    if not os.path.exists(source_directory):
        raise OSError("Source directory does not exist")
    # Create the zip file
    with zipfile.ZipFile(target_directory + "/" + zip_name + ".zip", "w", zipfile.ZIP_STORED) as zf:
        # Iterate over the files in the source directory
        for file in glob.glob(source_directory + "/*"):
            # Check if the file is a valid extension
            if os.path.splitext(file)[1] in [".txt", ".docx", ".xlsx", ".csv"]:
                # Add the file to the zip file
                zf.write(file)
    return target_directory + "/" + zip_name + ".zip"