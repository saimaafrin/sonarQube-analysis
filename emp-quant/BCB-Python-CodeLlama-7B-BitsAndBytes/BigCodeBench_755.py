
import os
import glob

def task_func(directory_path):
    # Get a list of all files in the directory
    files = glob.glob(os.path.join(directory_path, '*'))

    # Initialize an empty list to store the new filenames
    new_filenames = []

    # Iterate over the files and reverse the order of the words in each filename
    for file in files:
        filename = os.path.basename(file)
        words = filename.split('.')
        new_filename = '.'.join(words[::-1])
        new_filenames.append(new_filename)

    return new_filenames