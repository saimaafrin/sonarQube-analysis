import warnings
import os
import glob
import shutil
import time
def task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS):
    transferred_files = []
    for extension in EXTENSIONS:
        # Create a pattern to match files with the specified extension
        pattern = os.path.join(SOURCE_DIR, f'*.{extension}')
        # Find all files matching the pattern
        files = glob.glob(pattern)
        for file in files:
            try:
                # Construct the destination path for the file
                dest_file = os.path.join(DEST_DIR, os.path.basename(file))
                # Transfer the file
                shutil.move(file, dest_file)
                transferred_files.append(os.path.basename(file))
            except Exception as e:
                # Issue a warning if the file could not be transferred
                warnings.warn(f"Failed to transfer {file}: {e}")
    return transferred_files