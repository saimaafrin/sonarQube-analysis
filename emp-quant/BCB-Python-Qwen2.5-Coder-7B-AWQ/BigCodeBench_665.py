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

    # Iterate over all patterns
    for pattern in patterns:
        # Find all files matching the pattern in the source directory
        for filename in fnmatch.filter(os.listdir(src_dir), pattern):
            # Construct full file path
            src_file = os.path.join(src_dir, filename)
            # Construct full destination file path
            dst_file = os.path.join(dst_dir, filename)
            # Copy the file to the destination directory
            shutil.copy2(src_file, dst_file)

    # Return the destination directory
    return dst_dir