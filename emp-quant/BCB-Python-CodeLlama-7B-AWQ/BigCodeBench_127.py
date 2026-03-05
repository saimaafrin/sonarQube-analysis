import os
import shutil
import glob
import hashlib
def task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH):
    """
    Moves all files from a specified root directory (ROOT_DIR) to a target directory (DEST_DIR) if they match a specific hash value (SPECIFIC_HASH).
    The function calculates the MD5 hash of each file in ROOT_DIR and moves it if the hash matches SPECIFIC_HASH.
    """
    # Ensure the existence of the root directory
    if not os.path.exists(ROOT_DIR):
        raise FileNotFoundError(f"Root directory {ROOT_DIR} does not exist.")

    # Ensure the existence of the target directory
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    # Calculate the MD5 hash of each file in ROOT_DIR
    file_hashes = {}
    for file in glob.glob(os.path.join(ROOT_DIR, "**", "*")):
        with open(file, "rb") as f:
            file_hashes[file] = hashlib.md5(f.read()).hexdigest()

    # Move files with matching hashes to DEST_DIR
    moved_files = 0
    for file, hash in file_hashes.items():
        if hash == SPECIFIC_HASH:
            shutil.move(file, os.path.join(DEST_DIR, os.path.basename(file)))
            moved_files += 1

    return moved_files
ROOT_DIR = "."
DEST_DIR = "dest"
SPECIFIC_HASH = "1234567890abcdef"