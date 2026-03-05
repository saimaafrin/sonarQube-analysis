import os
import logging
def task_func(directory):
    """
    Removes all jQuery files (JavaScript files containing 'jquery' in their name) from a specified directory.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    jquery_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if "jquery" in file:
                jquery_files.append(os.path.join(root, file))

    removed_files = []
    for file in jquery_files:
        try:
            os.remove(file)
            removed_files.append(file)
        except FileNotFoundError:
            logging.warning(f"File {file} does not exist")

    return len(removed_files), removed_files