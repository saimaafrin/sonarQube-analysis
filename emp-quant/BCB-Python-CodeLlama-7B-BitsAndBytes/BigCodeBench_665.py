
import shutil
import os
import fnmatch
import itertools

def task_func(src_dir, dst_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # Get a list of all files in the source directory that match the patterns
    src_files = [os.path.join(src_dir, f) for f in os.listdir(src_dir) if any(fnmatch.fnmatch(f, pattern) for pattern in ['*.txt', '*.docx'])]

    # Copy the files to the destination directory
    for src_file in src_files:
        dst_file = os.path.join(dst_dir, os.path.basename(src_file))
        shutil.copy(src_file, dst_file)

    return dst_dir