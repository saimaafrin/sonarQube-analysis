import re
import os
import glob
import mimetypes
def task_func(directory, file_pattern, suffix):
    # Initialize an empty dictionary to store file names and their MIME types
    file_mime_types = {}
    
    # Use glob to find all files in the directory that match the pattern and suffix
    for file_path in glob.glob(os.path.join(directory, f"{file_pattern}*.{suffix}")):
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)
        
        # Use mimetypes to guess the MIME type of the file
        mime_type, _ = mimetypes.guess_type(file_path)
        
        # Add the file name and its MIME type to the dictionary
        file_mime_types[file_name] = mime_type
    
    # Return the dictionary containing file names and their MIME types
    return file_mime_types