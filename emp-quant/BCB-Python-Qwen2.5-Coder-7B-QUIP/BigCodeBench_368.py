
import os
import shutil
import random

def task_func(src_dir: str, dest_dir: str, seed: int = 100) -> str:
    # Set the random seed for reproducibility
    random.seed(seed)

    # Get a list of all files in the source directory
    files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]

    # If there are no files, return an empty string
    if not files:
        return ""

    # Select a random file from the list
    random_file = random.choice(files)

    # Construct the full path of the source file
    src_file = os.path.join(src_dir, random_file)

    # Construct the full path of the destination file
    dest_file = os.path.join(dest_dir, random_file)

    # Move the file from the source directory to the destination directory
    shutil.move(src_file, dest_file)

    # Return the name of the moved file
    return random_file