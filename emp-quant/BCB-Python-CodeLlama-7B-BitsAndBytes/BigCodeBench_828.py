
import os
import errno
import shutil

def task_func(filename, dest_dir):
    # Check if the destination directory exists
    if not os.path.exists(dest_dir):
        raise OSError("Destination directory does not exist")

    # Get the absolute path of the destination directory
    dest_dir_abs_path = os.path.abspath(dest_dir)

    # Copy the file to the destination directory
    shutil.copy(filename, dest_dir_abs_path)

    # Clear the contents of the original file
    with open(filename, 'w') as f:
        f.truncate()

    # Return the absolute path of the copied file
    return os.path.join(dest_dir_abs_path, os.path.basename(filename))