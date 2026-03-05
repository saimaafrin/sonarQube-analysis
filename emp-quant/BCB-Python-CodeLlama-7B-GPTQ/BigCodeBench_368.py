import os
import shutil
import random
def task_func(src_dir: str, dest_dir: str, seed: int = 100) -> str:
    """
    Moves a random file from the source directory to the specified destination directory.
    The function should output with:
        str: The name of the file moved. Format: 'filename.extension' (e.g., 'file1.txt').
    """
    # Get a list of all files in the source directory
    file_list = os.listdir(src_dir)
    # Randomly select a file from the list
    file_name = random.choice(file_list)
    # Move the selected file to the destination directory
    shutil.move(os.path.join(src_dir, file_name), dest_dir)
    # Return the name of the file moved
    return file_name
src_dir = 'source_dir'
dest_dir = 'dest_dir'