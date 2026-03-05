
import os
import shutil
import random

def task_func(src_dir: str, dest_dir: str, seed:int = 100) -> str:
    # Set the random seed for reproducibility
    random.seed(seed)

    # Get the list of files in the source directory
    files = os.listdir(src_dir)

    # Select a random file from the list
    file_name = random.choice(files)

    # Move the selected file to the destination directory
    shutil.move(os.path.join(src_dir, file_name), dest_dir)

    # Return the name of the moved file
    return file_name