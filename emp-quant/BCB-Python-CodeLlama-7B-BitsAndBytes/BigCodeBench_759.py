
import os
import shutil
import fnmatch

def task_func(source_directory, destination_directory, file_pattern):
    # Create a list to store the moved filenames
    moved_filenames = []

    # Iterate over the files in the source directory
    for filename in os.listdir(source_directory):
        # Check if the filename matches the pattern
        if fnmatch.fnmatch(filename, file_pattern):
            # Move the file to the destination directory
            shutil.move(os.path.join(source_directory, filename), os.path.join(destination_directory, filename))
            # Add the filename to the list of moved filenames
            moved_filenames.append(filename)

    # Return the list of moved filenames
    return moved_filenames