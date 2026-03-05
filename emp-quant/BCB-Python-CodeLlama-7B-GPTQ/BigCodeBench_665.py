import shutil
import os
import fnmatch
import itertools
def task_func(src_dir, dst_dir):
    """
    Copy all files from 'src_dir' to 'dst_dir' that match any pattern in ['*.txt', '*.docx'].
    """
    # Check if the source directory exists
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")

    # Check if the destination directory exists
    if not os.path.exists(dst_dir):
        raise FileNotFoundError(f"Destination directory '{dst_dir}' does not exist.")

    # Get a list of all files in the source directory that match the patterns
    src_files = [os.path.join(src_dir, f) for f in os.listdir(src_dir) if fnmatch.fnmatch(f, '*.txt') or fnmatch.fnmatch(f, '*.docx')]

    # Copy the files to the destination directory
    for src_file in src_files:
        dst_file = os.path.join(dst_dir, os.path.basename(src_file))
        shutil.copy(src_file, dst_file)

    # Return the destination directory
    return dst_dir
src_dir = 'src'
dst_dir = 'dst'