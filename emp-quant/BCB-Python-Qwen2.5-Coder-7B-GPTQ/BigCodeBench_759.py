import os
import shutil
import fnmatch
def task_func(source_directory, destination_directory, file_pattern):
    moved_files = []
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Iterate over all files in the source directory
    for filename in os.listdir(source_directory):
        # Check if the file matches the pattern
        if fnmatch.fnmatch(filename, file_pattern):
            # Construct full file path
            full_file_path = os.path.join(source_directory, filename)
            # Move the file to the destination directory
            shutil.move(full_file_path, destination_directory)
            # Add the filename to the list of moved files
            moved_files.append(filename)
    
    return moved_files