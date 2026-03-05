
import re
import os
import shutil

def task_func(directory):
    # Create a dictionary to hold directories for each extension
    extensions_dict = {}

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Extract the extension from the filename
        extension = os.path.splitext(filename)[1]
        if extension not in extensions_dict:
            # If the extension is not in the dictionary, create a new directory for it
            new_dir = os.path.join(directory, extension[1:])  # Remove the dot from the extension
            os.makedirs(new_dir)
            extensions_dict[extension] = new_dir

        # Move the file to the directory corresponding to its extension
        shutil.move(os.path.join(directory, filename), os.path.join(extensions_dict[extension], filename))

    return None