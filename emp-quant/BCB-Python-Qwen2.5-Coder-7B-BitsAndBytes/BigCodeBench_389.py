
import re
import os
import shutil

def task_func(directory):
    # Define the pattern to search for filenames containing "like" or "what"
    pattern = re.compile(r'like|what')
    
    # Create the new subdirectory if it doesn't exist
    new_subdir = os.path.join(directory, 'Interesting Files')
    if not os.path.exists(new_subdir):
        os.makedirs(new_subdir)
    
    # List to store the names of the files moved
    moved_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the filename contains "like" or "what"
            if pattern.search(file):
                # Construct the full path of the file
                old_file_path = os.path.join(root, file)
                # Move the file to the new subdirectory
                new_file_path = os.path.join(new_subdir, file)
                shutil.move(old_file_path, new_file_path)
                # Add the file name to the list of moved files
                moved_files.append(file)
    
    # Output the list of files moved
    print("List of files moved:")
    for file in moved_files:
        print(file)