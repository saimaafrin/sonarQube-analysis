import os
import shutil
import glob
import hashlib
def task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH):
    # Ensure the destination directory exists
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    # Initialize a counter for moved files
    moved_files_count = 0

    # Iterate over all files in the root directory
    for file_path in glob.glob(os.path.join(ROOT_DIR, '*')):
        if os.path.isfile(file_path):
            # Calculate the MD5 hash of the file
            with open(file_path, 'rb') as file:
                file_hash = hashlib.md5(file.read()).hexdigest()

            # Check if the hash matches the specific hash
            if file_hash == SPECIFIC_HASH:
                # Move the file to the destination directory
                shutil.move(file_path, os.path.join(DEST_DIR, os.path.basename(file_path)))
                moved_files_count += 1

    # Return the number of files moved
    return moved_files_count