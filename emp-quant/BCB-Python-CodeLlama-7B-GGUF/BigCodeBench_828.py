
import os
import errno
import shutil

def task_func(filename, dest_dir):
    # Check if destination directory exists
    if not os.path.exists(dest_dir):
        raise OSError(errno.ENOENT, "Destination directory does not exist")

    # Get the absolute path of the file
    file_path = os.path.abspath(filename)

    # Get the absolute path of the destination directory
    dest_dir_path = os.path.abspath(dest_dir)

    # Copy the file to the destination directory
    shutil.copy(file_path, dest_dir_path)

    # Clear the content of the original file
    with open(file_path, "w"):
        pass

    # Return the absolute path of the copied file
    return os.path.join(dest_dir_path, os.path.basename(file_path))