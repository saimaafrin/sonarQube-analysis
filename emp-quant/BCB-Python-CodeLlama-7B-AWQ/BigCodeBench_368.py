import os
import shutil
import random
def task_func(src_dir: str, dest_dir: str, seed: int = 100) -> str:
    """
    Moves a random file from the source directory to the specified destination directory.
    """
    # Set the random seed
    random.seed(seed)

    # Get a list of all files in the source directory
    files = os.listdir(src_dir)

    # Select a random file from the list
    file_to_move = random.choice(files)

    # Move the file to the destination directory
    shutil.move(os.path.join(src_dir, file_to_move), dest_dir)

    # Return the name of the file moved
    return file_to_move
src_dir = 'source_dir'
dest_dir = 'dest_dir'