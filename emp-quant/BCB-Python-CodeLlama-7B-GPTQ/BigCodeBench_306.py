import os
import logging
def task_func(directory):
    """
    Removes all jQuery files (JavaScript files containing 'jquery' in their name) from a specified directory.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist.")

    jquery_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if "jquery" in file:
                jquery_files.append(os.path.join(root, file))

    for file in jquery_files:
        os.remove(file)

    logging.info(f"Removed {len(jquery_files)} jQuery files from {directory}.")

    return len(jquery_files), jquery_files
directory = "path/to/directory"