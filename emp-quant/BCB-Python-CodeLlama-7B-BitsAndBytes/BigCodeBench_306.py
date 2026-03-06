
import os
import logging

def task_func(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    # Create a list to store the names of the removed files
    removed_files = []

    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Check if the file name contains 'jquery'
        if 'jquery' in file:
            # Remove the file
            os.remove(os.path.join(directory, file))
            # Add the file name to the list of removed files
            removed_files.append(file)

    # Log the removed files
    logging.info(f"Removed {len(removed_files)} files: {', '.join(removed_files)}")

    # Return a tuple containing the number of files removed and the list of removed files
    return len(removed_files), removed_files