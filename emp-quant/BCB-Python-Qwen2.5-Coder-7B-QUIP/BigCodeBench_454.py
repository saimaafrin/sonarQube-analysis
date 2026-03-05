
import os
import shutil
import glob

def task_func(src_dir, dest_dir, ext):
    # Check if source directory exists
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory {src_dir} does not exist")
    
    # Check if destination directory exists
    if not os.path.exists(dest_dir):
        raise FileNotFoundError(f"Destination directory {dest_dir} does not exist")
    
    # Initialize a list to store the paths of moved files
    moved_files = []
    
    # Get a list of files with the specified extension in the source directory
    files_to_move = glob.glob(os.path.join(src_dir, f"*.{ext}"))
    
    # Move each file to the destination directory
    for file_path in files_to_move:
        # Get the base name of the file
        base_name = os.path.basename(file_path)
        
        # Create the destination file path
        dest_file_path = os.path.join(dest_dir, base_name)
        
        # Check if the file already exists in the destination directory
        if os.path.exists(dest_file_path):
            continue
        
        # Move the file to the destination directory
        shutil.move(file_path, dest_file_path)
        
        # Add the moved file path to the list
        moved_files.append(file_path)
    
    # Return the list of moved file paths
    return moved_files