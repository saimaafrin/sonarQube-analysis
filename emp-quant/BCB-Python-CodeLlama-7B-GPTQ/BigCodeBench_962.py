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

    # Get a list of files in the source directory
    files = glob.glob(os.path.join(source_directory, "**", "*.txt"), recursive=True)
    files.extend(glob.glob(os.path.join(source_directory, "**", "*.docx"), recursive=True))
    files.extend(glob.glob(os.path.join(source_directory, "**", "*.xlsx"), recursive=True))
    files.extend(glob.glob(os.path.join(source_directory, "**", "*.csv"), recursive=True))

    # Move files to the target directory
    moved_files = 0
    for file in files:
        # Get the file name and extension
        file_name, file_extension = os.path.splitext(file)
        file_extension = file_extension.lstrip(".")

        # Check if the file already exists in the target directory
        target_file = os.path.join(target_directory, file_name + file_extension)
        if os.path.exists(target_file):
            # Rename the file if it already exists
            new_file_name = f"{file_name}-{moved_files}{file_extension}"
            target_file = os.path.join(target_directory, new_file_name)
            moved_files += 1

        # Move the file to the target directory
        shutil.move(file, target_file)

    # Return the number of files moved
    return moved_files
source_directory = "source_directory"
target_directory = "target_directory"