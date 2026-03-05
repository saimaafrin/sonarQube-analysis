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
            # Create the path to the source file
            src_path = os.path.join(directory, filename)
            # Create the path to the destination directory
            dst_dir = os.path.join(directory, 'Interesting Files')
            # Create the destination directory if it does not exist
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            # Create the path to the destination file
            dst_path = os.path.join(dst_dir, filename)
            # Move the file to the destination directory
            shutil.move(src_path, dst_path)
            # Add the filename to the list of moved files
            moved_files.append(filename)
    
    # Return the list of moved files
    return moved_files