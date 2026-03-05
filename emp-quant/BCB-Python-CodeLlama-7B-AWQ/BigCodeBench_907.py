import os
import re
def task_func(pattern: str, replacement: str, directory: str) -> bool:
    """
    Renames all files in a directory that match a particular pattern with a given replacement string.
    Returns a boolean value. True if the operation was successful, otherwise False.
    """
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist")
        return False

    # Check if the pattern is a valid regular expression
    try:
        re.compile(pattern)
    except re.error as e:
        print(f"Invalid regular expression: {e}")
        return False

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file matches the pattern
        if re.match(pattern, filename):
            # Replace the file name with the replacement string
            new_filename = re.sub(pattern, replacement, filename)
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

    return True