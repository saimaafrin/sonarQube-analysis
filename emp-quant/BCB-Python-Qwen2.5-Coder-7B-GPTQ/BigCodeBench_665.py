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

    # Walk through the source directory
    for root, dirs, files in os.walk(src_dir):
        for pattern in patterns:
            # Find files that match the pattern
            for file in fnmatch.filter(files, pattern):
                # Construct full file path
                src_file = os.path.join(root, file)
                # Construct destination file path
                dst_file = os.path.join(dst_dir, file)
                # Copy the file to the destination directory
                shutil.copy2(src_file, dst_file)

    # Return the destination directory
    return dst_dir