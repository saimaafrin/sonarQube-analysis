
import os
import shutil
import fnmatch

def task_func(source_directory, destination_directory, file_pattern):
    """
    Moves files from 'source_directory' to 'destination_directory' based on a filename pattern 'file_pattern'.
    
    Parameters:
    source_directory (str): The directory from which files will be moved.
    destination_directory (str): The directory to which files will be moved.
    file_pattern (str): The pattern to match filenames.
    
    Returns:
    list: A list of filenames that were moved.
    """
    moved_files = []
    
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(source_directory):
        for filename in fnmatch.filter(files, file_pattern):
            # Construct full file path
            full_file_path = os.path.join(root, filename)
            # Move the file to the destination directory
            shutil.move(full_file_path, os.path.join(destination_directory, filename))
            # Add the filename to the list of moved files
            moved_files.append(filename)
    
    return moved_files