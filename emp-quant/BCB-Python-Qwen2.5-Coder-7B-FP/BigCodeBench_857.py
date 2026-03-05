import warnings
import os
import glob
import shutil
import time
def task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS):
    transferred_files = []
    for ext in EXTENSIONS:
        # Use glob to find all files with the specified extension in the source directory
        files = glob.glob(os.path.join(SOURCE_DIR, f'*.{ext}'))
        for file in files:
            try:
                # Construct the destination path for the file
                dest_file = os.path.join(DEST_DIR, os.path.basename(file))
                # Transfer the file using shutil.move
                shutil.move(file, dest_file)
                transferred_files.append(os.path.basename(file))
            except Exception as e:
                # Issue a warning if the file could not be transferred
                warnings.warn(f"Failed to transfer {file}: {e}")
    return transferred_files