import os
import errno
import shutil
def task_func(filename, dest_dir):
    """
    Copies a file to a specified destination directory and clears its contents.
    """
    # Check if the destination directory exists
    if not os.path.exists(dest_dir):
        raise OSError(errno.ENOENT, "Destination directory does not exist")

    # Check if the destination directory is a file
    if os.path.isfile(dest_dir):
        raise OSError(errno.EISDIR, "Destination is a file, not a directory")

    # Check if the file exists
    if not os.path.exists(filename):
        raise OSError(errno.ENOENT, "File does not exist")

    # Check if the file is a directory
    if os.path.isdir(filename):
        raise OSError(errno.EISDIR, "File is a directory, not a file")

    # Copy the file to the destination directory
    shutil.copy(filename, dest_dir)

    # Clear the contents of the original file
    with open(filename, "w") as f:
        f.truncate()

    # Return the absolute path to the copied file within the destination directory
    return os.path.join(dest_dir, os.path.basename(filename))