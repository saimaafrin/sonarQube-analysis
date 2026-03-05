import os
import shutil
import glob
def task_func(source_dir, dest_dir, extension):
    """
    Moves all files with a particular extension from one directory to another.

    Parameters:
    source_dir (str): The directory to move files from.
    dest_dir (str): The directory to move files to.
    extension (str): The file extension to filter by (e.g., '.txt').

    Returns:
    result (int): The count of files that were moved.
    """
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Find all files with the specified extension in the source directory
    files_to_move = glob.glob(os.path.join(source_dir, f'*{extension}'))

    # Move each file to the destination directory
    for file_path in files_to_move:
        shutil.move(file_path, dest_dir)

    # Return the count of files moved
    return len(files_to_move)