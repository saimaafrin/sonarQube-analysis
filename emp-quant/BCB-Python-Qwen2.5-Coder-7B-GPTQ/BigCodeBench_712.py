import os
import shutil
import glob
def task_func(source_dir, dest_dir, extension):
    # Initialize the count of moved files
    moved_files_count = 0
    
    # Use glob to find all files with the specified extension in the source directory
    files_to_move = glob.glob(os.path.join(source_dir, f'*.{extension}'))
    
    # Iterate over the list of files and move them to the destination directory
    for file_path in files_to_move:
        # Construct the destination file path
        dest_file_path = os.path.join(dest_dir, os.path.basename(file_path))
        
        # Move the file
        shutil.move(file_path, dest_file_path)
        
        # Increment the count of moved files
        moved_files_count += 1
    
    # Return the count of moved files
    return moved_files_count