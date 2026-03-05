
import os
import shutil
import glob

def task_func(source_dir, dest_dir, extension):
    """
    Moves all files with a particular extension from one directory to another.

    Parameters:
    source_dir (str): The directory to move files from.
    dest_dir (str): The directory to move files to.
    extension (str): The file extension to move (e.g., '.txt').

    Returns:
    result (int): The count of files that were moved.
    """
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Initialize the count of moved files
    moved_count = 0

    # Use glob to find all files with the specified extension in the source directory
    for file_path in glob.glob(os.path.join(source_dir, f'*{extension}')):
        # Move the file to the destination directory
        shutil.move(file_path, dest_dir)
        moved_count += 1

    return moved_count