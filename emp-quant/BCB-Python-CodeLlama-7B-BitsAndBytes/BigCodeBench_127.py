
import os
import shutil
import glob
import hashlib

def task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH):
    # Calculate the MD5 hash of each file in ROOT_DIR
    file_hashes = {}
    for file in glob.glob(os.path.join(ROOT_DIR, '*')):
        with open(file, 'rb') as f:
            file_hashes[file] = hashlib.md5(f.read()).hexdigest()

    # Move files with the specified hash to DEST_DIR
    num_files_moved = 0
    for file, hash in file_hashes.items():
        if hash == SPECIFIC_HASH:
            shutil.move(file, os.path.join(DEST_DIR, os.path.basename(file)))
            num_files_moved += 1

    return num_files_moved