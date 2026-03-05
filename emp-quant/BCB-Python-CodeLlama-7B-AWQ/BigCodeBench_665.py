import shutil
import os
import fnmatch
import itertools
def task_func(src_dir, dst_dir):
    """
    Copy all files from 'src_dir' to 'dst_dir' that match any pattern in ['*.txt', '*.docx'].
    """
    # Create a list of all files in the source directory that match the patterns
    src_files = [os.path.join(src_dir, f) for f in os.listdir(src_dir) if fnmatch.fnmatch(f, '*.txt') or fnmatch.fnmatch(f, '*.docx')]

    # Create a list of all files in the destination directory
    dst_files = [os.path.join(dst_dir, f) for f in os.listdir(dst_dir)]

    # Copy only the files that do not already exist in the destination directory
    for src_file in src_files:
        dst_file = os.path.join(dst_dir, os.path.basename(src_file))
        if dst_file not in dst_files:
            shutil.copy(src_file, dst_dir)

    return dst_dir
src_dir = 'src'
dst_dir = 'dst'