import re
import os
import shutil
def task_func(directory):
    # Define the pattern to search for filenames containing "like" or "what"
    pattern = re.compile(r'like|what')
    
    # List to store the names of the files moved
    moved_files = []
    
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        # Check if the filename contains "like" or "what"
        if pattern.search(filename):
            # Construct the full path of the file
            file_path = os.path.join(directory, filename)
            
            # Construct the path for the new subdirectory
            new_subdirectory = os.path.join(directory, 'Interesting Files')
            
            # Create the new subdirectory if it doesn't exist
            if not os.path.exists(new_subdirectory):
                os.makedirs(new_subdirectory)
            
            # Construct the full path for the new location of the file
            new_file_path = os.path.join(new_subdirectory, filename)
            
            # Move the file to the new location
            shutil.move(file_path, new_file_path)
            
            # Add the filename to the list of moved files
            moved_files.append(filename)
    
    # Return the list of files moved
    return moved_files