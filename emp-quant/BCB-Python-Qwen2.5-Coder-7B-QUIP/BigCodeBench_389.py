
import re
import os
import shutil

def task_func(directory):
    # Define the new subdirectory name
    new_subdir = "Interesting Files"
    
    # Create the new subdirectory if it doesn't exist
    if not os.path.exists(new_subdir):
        os.makedirs(new_subdir)
    
    # List of files moved
    moved_files = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the filename contains "like" or "what"
        if re.search(r'\b(like|what)\b', filename, re.IGNORECASE):
            # Construct the full file path
            full_path = os.path.join(directory, filename)
            # Move the file to the new subdirectory
            shutil.move(full_path, os.path.join(new_subdir, filename))
            # Add the filename to the list of moved files
            moved_files.append(filename)
    
    # Output the list of files moved
    print("List of files moved:")
    for file in moved_files:
        print(file)