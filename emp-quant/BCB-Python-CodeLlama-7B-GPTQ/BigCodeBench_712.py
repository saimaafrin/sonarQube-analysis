import os
import shutil
import glob
def task_func(source_dir, dest_dir, extension):
    """
    Move all files with a particular extension from one directory to another.
    """
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory {source_dir} does not exist")

    # Check if the destination directory exists
    if not os.path.exists(dest_dir):
        raise ValueError(f"Destination directory {dest_dir} does not exist")

    # Check if the extension is valid
    if not extension.startswith("."):
        raise ValueError(f"Invalid extension {extension}")

    # Get a list of files with the specified extension in the source directory
    files = glob.glob(os.path.join(source_dir, f"*{extension}"))

    # Move the files to the destination directory
    for file in files:
        shutil.move(file, os.path.join(dest_dir, os.path.basename(file)))

    # Return the count of files that were moved
    return len(files)
source_dir = "source_dir"
dest_dir = "dest_dir"
extension = ".txt"