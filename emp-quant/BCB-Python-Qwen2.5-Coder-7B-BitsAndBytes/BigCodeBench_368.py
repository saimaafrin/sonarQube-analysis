
import os
import shutil
import random

def task_func(src_dir: str, dest_dir: str, seed: int = 100) -> str:
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # List all files in the source directory
    files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
    
    # If there are no files in the source directory, return an empty string
    if not files:
        return ""
    
    # Select a random file
    selected_file = random.choice(files)
    
    # Construct full paths for the source and destination files
    src_file_path = os.path.join(src_dir, selected_file)
    dest_file_path = os.path.join(dest_dir, selected_file)
    
    # Move the file from the source directory to the destination directory
    shutil.move(src_file_path, dest_file_path)
    
    # Return the name of the moved file
    return selected_file