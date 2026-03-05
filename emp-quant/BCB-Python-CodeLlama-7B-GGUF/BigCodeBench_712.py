
import os
import shutil
import glob

def task_func(source_dir, dest_dir, extension):
    """
    Move all files with a particular extension from one directory to another.

    Args:
        source_dir (str): The source directory.
        dest_dir (str): The destination directory.
        extension (str): The file extension to move.

    Returns:
        result (int): The count of files that were moved.
    """
    result = 0
    for file in glob.glob(os.path.join(source_dir, '*.' + extension)):
        shutil.move(file, dest_dir)
        result += 1
    return result