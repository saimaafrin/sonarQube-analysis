import os
from pathlib import Path
import glob
import shutil
def task_func(source_directory: str, target_directory: str):
    """
    Moves files with specific extensions from a source directory to a target directory, handling naming conflicts by renaming duplicates.
    """
    # Check if source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory {source_directory} does not exist")

    # Get list of files in source directory
    files = glob.glob(os.path.join(source_directory, "**", "*.txt"), recursive=True)
    files.extend(glob.glob(os.path.join(source_directory, "**", "*.docx"), recursive=True))
    files.extend(glob.glob(os.path.join(source_directory, "**", "*.xlsx"), recursive=True))
    files.extend(glob.glob(os.path.join(source_directory, "**", "*.csv"), recursive=True))

    # Move files to target directory
    moved_files = 0
    for file in files:
        # Get file name and extension
        file_name, file_extension = os.path.splitext(file)
        # Check if file exists in target directory
        if os.path.exists(os.path.join(target_directory, file_name + file_extension)):
            # Rename file if it exists in target directory
            file_name += "-" + str(moved_files)
            moved_files += 1
        # Move file to target directory
        shutil.move(file, os.path.join(target_directory, file_name + file_extension))

    return moved_files