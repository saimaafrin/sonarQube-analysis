import shutil
import os
import fnmatch
import itertools
def task_func(src_dir, dst_dir):
    """
    Copy all files from 'src_dir' to 'dst_dir' that match any pattern in ['*.txt', '*.docx'].
    """
    # Create a list of all files in the source directory
    src_files = os.listdir(src_dir)

    # Create a list of all files in the destination directory
    dst_files = os.listdir(dst_dir)

    # Create a list of all files that match the patterns in the list
    matching_files = [file for file in src_files if any(fnmatch.fnmatch(file, pattern) for pattern in ['*.txt', '*.docx'])]

    # Copy the matching files to the destination directory
    for file in matching_files:
        shutil.copy(os.path.join(src_dir, file), os.path.join(dst_dir, file))

    # Return the destination directory
    return dst_dir
src_dir = 'src'
dst_dir = 'dst'
src_files = os.listdir(src_dir)
dst_files = os.listdir(dst_dir)
matching_files = [file for file in src_files if any(fnmatch.fnmatch(file, pattern) for pattern in ['*.txt', '*.docx'])]