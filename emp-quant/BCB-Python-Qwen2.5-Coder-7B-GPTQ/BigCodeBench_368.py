import os
import shutil
import random
def task_func(src_dir: str, dest_dir: str, seed: int = 100) -> str:
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # List all files in the source directory
    files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
    
    # Check if there are any files in the source directory
    if not files:
        raise ValueError("No files found in the source directory.")
    
    # Select a random file from the list
    selected_file = random.choice(files)
    
    # Construct the full path of the selected file
    src_file_path = os.path.join(src_dir, selected_file)
    
    # Construct the full path for the destination file
    dest_file_path = os.path.join(dest_dir, selected_file)
    
    # Move the file from the source directory to the destination directory
    shutil.move(src_file_path, dest_file_path)
    
    # Return the name of the moved file
    return selected_file