
import re
import os
import glob
import mimetypes

def task_func(directory, file_pattern, suffix):
    """
    Scans a specified directory for files matching a given pattern and with a certain suffix,
    then determines their file types. Returns a dictionary with file names as keys and their
    corresponding MIME types as values.

    :param directory: str, the directory to scan
    :param file_pattern: str, the pattern to match in file names
    :param suffix: str, the file suffix to filter by
    :return: dict, a dictionary mapping file names to their MIME types
    """
    # Compile the regular expression for the file pattern
    pattern = re.compile(file_pattern)
    
    # Initialize an empty dictionary to store the results
    results = {}
    
    # Use glob to find all files in the directory that match the pattern and suffix
    for file_path in glob.glob(os.path.join(directory, f'*.{suffix}')):
        # Check if the file name matches the pattern
        if pattern.match(os.path.basename(file_path)):
            # Use mimetypes to determine the MIME type of the file
            mime_type, _ = mimetypes.guess_type(file_path)
            # Add the file name and MIME type to the results dictionary
            results[os.path.basename(file_path)] = mime_type
    
    return results