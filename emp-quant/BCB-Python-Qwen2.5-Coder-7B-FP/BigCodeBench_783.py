import os
import shutil
def task_func(src_dir, dest_dir, extension):
    """
    Moves all files with a particular extension from one directory to another.

    Parameters:
    src_dir (str): The source directory.
    dest_dir (str): The destination directory.
    extension (str): The file extension to move (e.g., '.txt').

    Returns:
    files_moved (int): The number of files moved.
    """
    # Initialize the count of files moved
    files_moved = 0

    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Walk through the source directory
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # Check if the file ends with the specified extension
            if file.endswith(extension):
                # Construct full file path
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, file)
                # Move the file
                shutil.move(src_file_path, dest_file_path)
                # Increment the count of files moved
                files_moved += 1

    return files_moved