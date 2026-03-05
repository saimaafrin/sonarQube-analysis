
import shutil
import os
import fnmatch
import itertools

def task_func(src_dir, dst_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # Get a list of all files in the source directory that match any pattern in ['*.txt', '*.docx']
    files = [f for f in os.listdir(src_dir) if fnmatch.fnmatch(f, '*.txt') or fnmatch.fnmatch(f, '*.docx')]

    # Copy the files to the destination directory
    for file in files:
        shutil.copy(os.path.join(src_dir, file), dst_dir)

    return dst_dir