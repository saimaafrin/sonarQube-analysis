import os
import logging
def task_func(directory):
    """
    Removes all jQuery files (JavaScript files containing 'jquery' in their name) from a specified directory.
    Note that: Removed files are logged in 'jquery_removal.log' file.
    The function should raise the exception for: If the specified directory does not exist the code would raise FileNotFoundError.
    The function should output with:
        tuple: A tuple containing two elements:
            int: The number of files removed.
            list: The names of the removed files.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    jquery_files = []
    removed_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if "jquery" in file:
                jquery_files.append(os.path.join(root, file))

    for file in jquery_files:
        os.remove(file)
        removed_files.append(file)

    logging.info(f"Removed {len(removed_files)} jQuery files from {directory}")
    return len(removed_files), removed_files