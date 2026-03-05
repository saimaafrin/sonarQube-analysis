
import shutil
import os
import fnmatch
import itertools

def task_func(src_dir, dst_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # Get a list of all files in the source directory
    files = os.listdir(src_dir)

    # Filter the list to only include files that match the patterns
    files = [f for f in files if any(fnmatch.fnmatch(f, pattern) for pattern in ['*.txt', '*.docx'])]

    # Copy the files to the destination directory
    for file in files:
        shutil.copy(os.path.join(src_dir, file), dst_dir)

    # Return the destination directory
    return dst_dir