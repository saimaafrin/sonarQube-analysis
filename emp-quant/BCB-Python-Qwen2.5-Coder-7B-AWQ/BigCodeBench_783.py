import os
import shutil
def task_func(src_dir, dest_dir, extension):
    """
    Moves all files with a particular extension from one directory to another.

    Parameters:
    src_dir (str): The source directory from which files will be moved.
    dest_dir (str): The destination directory to which files will be moved.
    extension (str): The file extension to filter files by.

    Returns:
    files_moved (int): The number of files moved.
    """
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Initialize the count of files moved
    files_moved = 0

    # Iterate over all files in the source directory
    for filename in os.listdir(src_dir):
        # Check if the file has the specified extension
        if filename.endswith(extension):
            # Construct full file path
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            # Move the file
            shutil.move(src_file, dest_file)
            # Increment the count of files moved
            files_moved += 1

    return files_moved