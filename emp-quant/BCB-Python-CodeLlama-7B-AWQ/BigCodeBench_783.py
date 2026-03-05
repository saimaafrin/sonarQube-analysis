import os
import shutil
def task_func(src_dir, dest_dir, extension):
    """
    Move all files with a particular extension from one directory to another.

    Args:
        src_dir (str): The source directory.
        dest_dir (str): The destination directory.
        extension (str): The file extension to move.

    Returns:
        files_moved (int): The number of files moved.
    """
    files_moved = 0
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(extension):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                shutil.move(src_file, dest_file)
                files_moved += 1
    return files_moved