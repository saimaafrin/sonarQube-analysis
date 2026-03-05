
import os
import re

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    """
    Renames all files in a directory that match a particular pattern with a given replacement string.

    Args:
        pattern (str): The pattern to match against.
        replacement (str): The replacement string to use.
        directory (str): The directory to search for files to rename.

    Returns:
        bool: True if the operation was successful, otherwise False.
    """
    try:
        for file in os.listdir(directory):
            if re.match(pattern, file):
                new_file = re.sub(pattern, replacement, file)
                os.rename(os.path.join(directory, file), os.path.join(directory, new_file))
        return True
    except Exception as e:
        print(f"Error renaming files: {e}")
        return False