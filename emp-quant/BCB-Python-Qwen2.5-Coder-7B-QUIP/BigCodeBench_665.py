
import shutil
import os
import fnmatch
import itertools

def task_func(src_dir, dst_dir):
    # Ensure the destination directory exists
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # List all files in the source directory that match the patterns
    matching_files = []
    for pattern in ['*.txt', '*.docx']:
        matching_files.extend(fnmatch.filter(os.listdir(src_dir), pattern))

    # Copy matching files to the destination directory
    for file_name in matching_files:
        shutil.copy(os.path.join(src_dir, file_name), dst_dir)

    return dst_dir