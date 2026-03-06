
import os
import re

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    """
    Renames all files in a directory that match a particular pattern with a given replacement string.

    Args:
        pattern (str): The pattern to match.
        replacement (str): The replacement string.
        directory (str): The directory to search in.

    Returns:
        bool: True if the operation was successful, otherwise False.
    """
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        return False

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Iterate over the files and rename them if necessary
    for file in files:
        if re.search(pattern, file):
            new_file = re.sub(pattern, replacement, file)
            os.rename(os.path.join(directory, file), os.path.join(directory, new_file))

    return True