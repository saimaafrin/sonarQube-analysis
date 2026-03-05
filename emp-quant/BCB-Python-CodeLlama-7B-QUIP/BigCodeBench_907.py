
import os
import re

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    """
    Renames all files in a directory that match a particular pattern with a given replacement string.
    Returns a boolean value. True if the operation was successful, otherwise False.
    """
    files = os.listdir(directory)
    for file in files:
        if re.match(pattern, file):
            new_file = re.sub(pattern, replacement, file)
            os.rename(os.path.join(directory, file), os.path.join(directory, new_file))
    return True