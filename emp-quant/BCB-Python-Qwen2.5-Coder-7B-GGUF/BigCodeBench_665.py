
import shutil
import os
import fnmatch
import itertools

def task_func(src_dir, dst_dir):
    # Ensure the destination directory exists
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # List of patterns to match
    patterns = ['*.txt', '*.docx']

    # Iterate over all files in the source directory
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # Check if the file matches any of the patterns
            if any(fnmatch.fnmatch(file, pattern) for pattern in patterns):
                # Construct the full file path
                src_file_path = os.path.join(root, file)
                # Construct the destination file path
                dst_file_path = os.path.join(dst_dir, file)
                # Copy the file to the destination directory
                shutil.copy2(src_file_path, dst_file_path)

    return dst_dir