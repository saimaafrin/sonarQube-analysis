import os
import re
def task_func(pattern: str, replacement: str, directory: str) -> bool:
    """
    Renames all files in a directory that match a particular pattern with a given replacement string.
    Returns a boolean value. True if the operation was successful, otherwise False.
    """
    if not os.path.isdir(directory):
        return False

    for filename in os.listdir(directory):
        if re.search(pattern, filename):
            new_filename = re.sub(pattern, replacement, filename)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

    return True
directory = "test_dir"
pattern = r"\.txt$"
replacement = r"\.py"