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
    # Set the random seed for reproducibility
    random.seed(seed)
    # Choose a random file from the list
    random_file = random.choice(file_list)
    # Move the file to the destination directory
    shutil.move(os.path.join(src_dir, random_file), dest_dir)
    # Return the name of the file moved
    return random_file
src_dir = 'source_directory'
dest_dir = 'destination_directory'