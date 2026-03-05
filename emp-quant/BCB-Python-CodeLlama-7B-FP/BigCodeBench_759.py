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

    # Iterate over the files in the source directory
    for file in os.listdir(source_directory):
        # Check if the file matches the pattern
        if fnmatch.fnmatch(file, file_pattern):
            # Move the file to the destination directory
            shutil.move(os.path.join(source_directory, file), destination_directory)
            # Add the moved filename to the list
            moved_files.append(file)

    # Return the list of moved filenames
    return moved_files
source_directory = "source_directory"
destination_directory = "destination_directory"
file_pattern = "*.txt"