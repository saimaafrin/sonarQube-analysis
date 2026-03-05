
import re
import os
import glob
import mimetypes

def task_func(directory, file_pattern, suffix):
    # Initialize an empty dictionary to store the results
    result = {}

    # Use glob to find files that match the pattern and suffix
    for filename in glob.glob(os.path.join(directory, f"{file_pattern}*.{suffix}")):
        # Use mimetypes to guess the MIME type of the file
        mime_type, _ = mimetypes.guess_type(filename)
        # Store the MIME type in the dictionary with the file name as the key
        result[filename] = mime_type

    # Return the dictionary
    return result