import os
import shutil
import fnmatch
def task_func(source_directory, destination_directory, file_pattern):
    moved_files = []
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(source_directory):
        for filename in fnmatch.filter(files, file_pattern):
            # Construct full file path
            full_file_path = os.path.join(root, filename)
            # Move the file to the destination directory
            shutil.move(full_file_path, destination_directory)
            # Append the moved file to the list
            moved_files.append(filename)
    
    return moved_files