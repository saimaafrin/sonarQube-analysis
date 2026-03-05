import os
import shutil
import glob
def task_func(src_dir, dest_dir, ext):
    # Check if source and destination directories exist
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")
    if not os.path.exists(dest_dir):
        raise FileNotFoundError(f"Destination directory '{dest_dir}' does not exist.")
    
    # List to store the paths of moved files
    moved_files = []
    
    # Search for files in the source directory with the specified extension
    for file_path in glob.glob(os.path.join(src_dir, f'*.{ext}')):
        # Extract the file name from the path
        file_name = os.path.basename(file_path)
        # Construct the destination file path
        dest_file_path = os.path.join(dest_dir, file_name)
        
        # Check if the file already exists in the destination directory
        if not os.path.exists(dest_file_path):
            # Move the file to the destination directory
            shutil.move(file_path, dest_file_path)
            # Add the moved file path to the list
            moved_files.append(dest_file_path)
    
    return moved_files