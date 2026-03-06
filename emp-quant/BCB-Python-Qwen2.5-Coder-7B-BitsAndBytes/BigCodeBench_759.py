
import os
import shutil
import fnmatch

def task_func(source_directory, destination_directory, file_pattern):
    """
    Moves all files that match a particular pattern from one directory to another.

    Parameters:
    source_directory (str): The path to the source directory.
    destination_directory (str): The path to the destination directory.
    file_pattern (str): The pattern to match against filenames.

    Returns:
    list: A list of filenames that were moved.
    """
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    moved_files = []

    # Walk through the source directory
    for root, dirs, files in os.walk(source_directory):
        for filename in fnmatch.filter(files, file_pattern):
            source_file_path = os.path.join(root, filename)
            destination_file_path = os.path.join(destination_directory, filename)
            
            # Move the file
            shutil.move(source_file_path, destination_file_path)
            moved_files.append(filename)

    return moved_files