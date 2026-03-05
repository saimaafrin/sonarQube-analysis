import os
import glob
def task_func(directory_path):
    new_filenames = []
    # Get all files in the directory
    files = glob.glob(os.path.join(directory_path, '*'))
    for file in files:
        # Check if it's a file and not a directory
        if os.path.isfile(file):
            # Split the filename by periods and reverse the order
            parts = file.split('.')
            reversed_parts = parts[::-1]
            # Join the reversed parts to form the new filename
            new_filename = '.'.join(reversed_parts)
            # Add the new filename to the list
            new_filenames.append(new_filename)
    return new_filenames