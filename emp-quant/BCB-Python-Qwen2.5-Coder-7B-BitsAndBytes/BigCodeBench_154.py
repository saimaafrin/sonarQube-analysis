
import re
import os
import glob
import mimetypes

def task_func(directory, file_pattern, suffix):
    """
    Scans a specified directory for files matching a given pattern and with a certain suffix,
    then determines their file types. Returns a dictionary with file names as keys and their
    corresponding MIME types as values.

    :param directory: str - The directory to scan.
    :param file_pattern: str - The regex pattern to match file names.
    :param suffix: str - The file suffix to filter by.
    :return: dict - A dictionary mapping file names to their MIME types.
    """
    # Compile the regex pattern for efficient matching
    pattern = re.compile(file_pattern)
    
    # Initialize an empty dictionary to store the results
    result = {}
    
    # Use glob to find all files in the directory that match the suffix
    for filename in glob.glob(os.path.join(directory, f'*.{suffix}')):
        # Check if the file name matches the given pattern
        if pattern.match(filename):
            # Determine the MIME type of the file
            mime_type, _ = mimetypes.guess_type(filename)
            # Add the file name and its MIME type to the result dictionary
            result[filename] = mime_type
    
    return result