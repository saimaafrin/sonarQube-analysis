import re
import os
import glob
from pathlib import Path
def task_func(pattern, directory, extensions):
    """
    Find all files in a specific directory that contain a regex pattern in their contents in a case insensitive manner.
    :param pattern: The regex pattern to search for.
    :param directory: The directory to search in.
    :param extensions: A list of file extensions to search for.
    :return: A list of absolute file paths that contain the pattern.
    """
    # Create a list to store the file paths
    file_paths = []

    # Iterate over the files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file has the specified extension
            if file.endswith(extensions):
                # Open the file and read its contents
                with open(os.path.join(root, file), 'r') as f:
                    contents = f.read()

                # Check if the pattern is in the contents
                if re.search(pattern, contents, re.IGNORECASE):
                    # Add the file path to the list
                    file_paths.append(os.path.join(root, file))

    # Return the list of file paths
    return file_paths