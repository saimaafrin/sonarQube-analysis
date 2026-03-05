import os
import shutil
import glob
def task_func(source_dir, dest_dir, extension):
    """
    Move all files with a particular extension from one directory to another.
    """
    # Check if source_dir and dest_dir are valid directories
    if not os.path.isdir(source_dir) or not os.path.isdir(dest_dir):
        raise ValueError("Invalid directory")

    # Check if extension is a valid string
    if not isinstance(extension, str):
        raise ValueError("Invalid extension")

    # Get a list of files with the specified extension in the source directory
    files = glob.glob(os.path.join(source_dir, f"*.{extension}"))

    # Move each file to the destination directory
    count = 0
    for file in files:
        shutil.move(file, dest_dir)
        count += 1

    return count
source_dir = "source_dir"
dest_dir = "dest_dir"
extension = "txt"