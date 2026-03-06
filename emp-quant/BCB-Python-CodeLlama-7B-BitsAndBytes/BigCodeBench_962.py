
import os
from pathlib import Path
import glob
import shutil

def task_func(source_directory: str, target_directory: str):
    # Check if source_directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"Source directory {source_directory} does not exist")

    # Get a list of all files in the source directory and its subdirectories
    file_list = glob.glob(os.path.join(source_directory, '**', '*'), recursive=True)

    # Filter the list to only include files with the desired extensions
    file_list = [file for file in file_list if file.endswith(('.txt', '.docx', '.xlsx', '.csv'))]

    # Initialize a counter for the number of files successfully moved
    num_files_moved = 0

    # Iterate over the filtered list of files
    for file in file_list:
        # Get the file name and extension
        file_name, file_extension = os.path.splitext(file)

        # Check if the file already exists in the target directory
        target_file = os.path.join(target_directory, file_name + file_extension)
        if os.path.exists(target_file):
            # If the file already exists, rename it with a unique name
            new_file_name = f"{file_name}-{num_files_moved}{file_extension}"
            target_file = os.path.join(target_directory, new_file_name)
            num_files_moved += 1

        # Move the file to the target directory
        shutil.move(file, target_file)

    # Return the number of files successfully moved
    return num_files_moved