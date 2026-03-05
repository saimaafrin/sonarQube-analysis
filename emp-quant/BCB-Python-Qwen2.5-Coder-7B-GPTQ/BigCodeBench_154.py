import re
import os
import glob
import mimetypes
def task_func(directory, file_pattern, suffix):
    # Compile the regular expression pattern for file matching
    pattern = re.compile(file_pattern)
    
    # Initialize an empty dictionary to store file names and their MIME types
    file_mime_types = {}
    
    # Use glob to find all files in the directory that match the pattern and have the specified suffix
    for file_path in glob.glob(os.path.join(directory, f'*.{suffix}')):
        # Check if the file name matches the given pattern
        if pattern.match(os.path.basename(file_path)):
            # Use mimetypes to determine the MIME type of the file
            mime_type, _ = mimetypes.guess_type(file_path)
            # Add the file name and its MIME type to the dictionary
            file_mime_types[os.path.basename(file_path)] = mime_type
    
    # Return the dictionary containing file names and their MIME types
    return file_mime_types