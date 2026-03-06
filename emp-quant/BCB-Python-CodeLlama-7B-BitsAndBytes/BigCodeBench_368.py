
import os
import shutil
import random

def task_func(src_dir: str, dest_dir: str, seed: int = 100) -> str:
    """
    Moves a random file from the source directory to the specified destination directory.

    Args:
        src_dir (str): The source directory.
        dest_dir (str): The destination directory.
        seed (int, optional): The random seed. Defaults to 100.

    Returns:
        str: The name of the file moved. Format: 'filename.extension' (e.g., 'file1.txt').
    """
    # Get a list of all files in the source directory
    file_list = os.listdir(src_dir)

    # Randomly select a file from the list
    random_file = random.choice(file_list)

    # Move the selected file to the destination directory
    shutil.move(os.path.join(src_dir, random_file), dest_dir)

    # Return the name of the file moved
    return random_file