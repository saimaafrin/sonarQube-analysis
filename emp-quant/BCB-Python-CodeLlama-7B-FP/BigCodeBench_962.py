import os
from pathlib import Path
import glob
import shutil
def task_func(source_directory: str, target_directory: str):
    """
    Moves files with specific extensions from a source directory to a target directory, handling naming conflicts by renaming duplicates.
    """
    # Check if source_directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory {source_directory} does not exist.")

    # Get a list of all files in the source directory and its subdirectories
    file_list = glob.glob(os.path.join(source_directory, "**", "*.txt"), recursive=True)
    file_list.extend(glob.glob(os.path.join(source_directory, "**", "*.docx"), recursive=True))
    file_list.extend(glob.glob(os.path.join(source_directory, "**", "*.xlsx"), recursive=True))
    file_list.extend(glob.glob(os.path.join(source_directory, "**", "*.csv"), recursive=True))

    # Move files to the target directory
    moved_files = 0
    for file in file_list:
        # Get the file name and extension
        file_name, file_extension = os.path.splitext(file)
        # Check if the file already exists in the target directory
        if os.path.exists(os.path.join(target_directory, file_name + file_extension)):
            # Rename the file with a unique name
            new_file_name = f"{file_name}-{moved_files}{file_extension}"
            moved_files += 1
            shutil.move(file, os.path.join(target_directory, new_file_name))
        else:
            shutil.move(file, os.path.join(target_directory, file_name + file_extension))

    return moved_files
source_directory = "C:\\source"
target_directory = "C:\\target"