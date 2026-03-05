
import os
import shutil
import fnmatch

def task_func(source_directory, destination_directory, file_pattern):
    """
    Moves all files that match a particular pattern from one directory to another.

    Args:
        source_directory (str): The source directory from which to move files.
        destination_directory (str): The destination directory to which to move files.
        file_pattern (str): The filename pattern to match.

    Returns:
        list[str]: A list of filenames that were moved.
    """
    moved_files = []
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if fnmatch.fnmatch(file, file_pattern):
                moved_files.append(file)
                shutil.move(os.path.join(root, file), destination_directory)
    return moved_files