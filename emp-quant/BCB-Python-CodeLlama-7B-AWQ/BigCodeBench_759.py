import os
import shutil
import fnmatch
def task_func(source_directory, destination_directory, file_pattern):
    """
    Moves all files that match a particular pattern from one directory to another.
    Functionality:
        - Moves files from 'source_directory' to 'destination_directory' based on a filename pattern 'file_pattern'.
    Returns a list of filenames that were moved.
    """
    # Create a list to store the moved filenames
    moved_files = []

    # Loop through the files in the source directory
    for filename in os.listdir(source_directory):
        # Check if the filename matches the pattern
        if fnmatch.fnmatch(filename, file_pattern):
            # Move the file to the destination directory
            shutil.move(os.path.join(source_directory, filename), os.path.join(destination_directory, filename))
            # Add the filename to the list of moved files
            moved_files.append(filename)

    # Return the list of moved files
    return moved_files
source_directory = 'source_dir'
destination_directory = 'destination_dir'
file_pattern = '*.txt'