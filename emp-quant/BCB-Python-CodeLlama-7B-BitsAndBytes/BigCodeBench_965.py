
import os
import re
import shutil

def task_func(source_directory: str, target_directory: str, pattern: str = r"\d{4}") -> int:
    """
    Moves files matching a specific regex pattern from a source directory to a target directory.

    Args:
        source_directory (str): The source directory to move files from.
        target_directory (str): The target directory to move files to.
        pattern (str, optional): The regex pattern to match files against. Defaults to r"\d{4}".

    Returns:
        int: The number of files successfully moved.
    """
    if not os.path.isdir(source_directory):
        return 0

    if not os.path.isdir(target_directory):
        os.makedirs(target_directory)

    files = os.listdir(source_directory)
    moved_files = 0
    for file in files:
        if re.match(pattern, file):
            shutil.move(os.path.join(source_directory, file), target_directory)
            moved_files += 1

    return moved_files