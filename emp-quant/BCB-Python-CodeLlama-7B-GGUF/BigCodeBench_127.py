
import os
import shutil
import glob
import hashlib

def task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH):
    # Calculate the MD5 hash of each file in ROOT_DIR
    file_hashes = {file: hashlib.md5(open(file, 'rb').read()).hexdigest() for file in glob.glob(os.path.join(ROOT_DIR, '*'))}

    # Move files with the specified hash to DEST_DIR
    moved_files = 0
    for file, hash in file_hashes.items():
        if hash == SPECIFIC_HASH:
            shutil.move(file, DEST_DIR)
            moved_files += 1

    return moved_files