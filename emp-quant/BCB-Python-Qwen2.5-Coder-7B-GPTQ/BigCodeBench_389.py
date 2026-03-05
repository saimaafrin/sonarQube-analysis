import re
import os
import shutil
def task_func(directory):
    # List to store the names of the files moved
    moved_files = []
    
    # Regular expression to match filenames containing "like" or "what"
    pattern = re.compile(r'like|what')
    
    # Create the new subdirectory if it doesn't exist
    new_directory = os.path.join(directory, 'Interesting Files')
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file name contains "like" or "what"
            if pattern.search(file):
                # Construct the full file path
                old_file_path = os.path.join(root, file)
                # Construct the new file path in the new subdirectory
                new_file_path = os.path.join(new_directory, file)
                # Move the file
                shutil.move(old_file_path, new_file_path)
                # Add the file name to the list of moved files
                moved_files.append(file)
    
    # Return the list of moved files
    return moved_files