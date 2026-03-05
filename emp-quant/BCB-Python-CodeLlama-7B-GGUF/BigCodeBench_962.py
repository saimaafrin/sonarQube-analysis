
import os
from pathlib import Path
import glob
import shutil

def task_func(source_directory: str, target_directory: str):
    # Check if source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory {source_directory} does not exist")

    # Get list of files in source directory
    file_list = glob.glob(os.path.join(source_directory, "*.txt"), recursive=True)
    file_list.extend(glob.glob(os.path.join(source_directory, "*.docx"), recursive=True))
    file_list.extend(glob.glob(os.path.join(source_directory, "*.xlsx"), recursive=True))
    file_list.extend(glob.glob(os.path.join(source_directory, "*.csv"), recursive=True))

    # Move files to target directory
    moved_files = 0
    for file in file_list:
        file_name = os.path.basename(file)
        target_file = os.path.join(target_directory, file_name)
        if os.path.exists(target_file):
            # Rename file if it already exists
            renamed_file = f"{file_name}-{moved_files}.{os.path.splitext(file_name)[1]}"
            target_file = os.path.join(target_directory, renamed_file)
            moved_files += 1
        shutil.move(file, target_file)
        moved_files += 1

    return moved_files