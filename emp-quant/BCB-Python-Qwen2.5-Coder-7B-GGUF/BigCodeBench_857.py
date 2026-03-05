
import warnings
import os
import glob
import shutil
import time

def task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS):
    transferred_files = []
    
    # Ensure the destination directory exists
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
    
    # Iterate over each extension provided
    for ext in EXTENSIONS:
        # Create a pattern to match files with the current extension
        pattern = os.path.join(SOURCE_DIR, f'*.{ext}')
        
        # Find all files matching the pattern
        files = glob.glob(pattern)
        
        # Iterate over each file found
        for file in files:
            try:
                # Construct the destination path for the file
                dest_file = os.path.join(DEST_DIR, os.path.basename(file))
                
                # Transfer the file
                shutil.move(file, dest_file)
                
                # Add the transferred file to the list
                transferred_files.append(os.path.basename(file))
                
                # Print a success message
                print(f"Transferred {file} to {dest_file}")
            except Exception as e:
                # Issue a warning if the file could not be transferred
                warnings.warn(f"Failed to transfer {file}: {e}")
    
    return transferred_files