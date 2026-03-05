import os
import re
import shutil
def task_func(source_directory: str, target_directory: str, pattern: str = r"\d{4}") -> int:
    """
    Moves files matching a specific regex pattern from a source directory to a target directory.
    Note that:
        - If source_directory does not exist or is not a directory, this function returns 0.
        - If target_directory does not exist, this function will create it.
    The function should output with:
        int: The number of files successfully moved.
    """
    if not os.path.isdir(source_directory):
        return 0

    # Create target directory if it does not exist
    if not os.path.isdir(target_directory):
        os.makedirs(target_directory)

    # Get list of files in source directory
    files = os.listdir(source_directory)

    # Filter files based on pattern
    files = [file for file in files if re.match(pattern, file)]

    # Move files to target directory
    for file in files:
        shutil.move(os.path.join(source_directory, file), os.path.join(target_directory, file))

    # Return number of files moved
    return len(files)
source_directory = "source"
target_directory = "target"
pattern = r"\d{4}"