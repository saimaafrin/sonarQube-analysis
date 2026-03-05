
import os
import shutil
import string
# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace

def task_func(directory_path):
    # Initialize a dictionary to keep track of the count of files moved to each directory
    summary = {}

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file has an invalid character in its name
        if any(char in INVALID_CHARACTERS for char in filename):
            # Move the file to the 'Invalid' directory
            shutil.move(os.path.join(directory_path, filename), os.path.join(directory_path, 'Invalid'))
            # Update the count of files moved to the 'Invalid' directory
            if 'Invalid' in summary:
                summary['Invalid'] += 1
            else:
                summary['Invalid'] = 1
        else:
            # If the file does not have an invalid character, do nothing
            pass

    # Return the summary dictionary
    return summary