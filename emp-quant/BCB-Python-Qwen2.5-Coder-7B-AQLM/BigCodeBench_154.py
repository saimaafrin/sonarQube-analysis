
import re
import os
import glob
import mimetypes

def task_func(directory, file_pattern, suffix):
    """
    Scans a specified directory for files matching a given pattern and with a certain suffix,
    then determines their file types. The function returns a dictionary with file names as keys
    and their corresponding MIME types as values.

    :param directory: The directory to scan for files.
    :param file_pattern: The pattern to match in the file names.
    :param suffix: The suffix to filter the files by.
    :return: A dictionary mapping file names to their MIME types.
    """
    # Initialize an empty dictionary to store file names and their MIME types
    file_mime_types = {}

    # Construct the full pattern to match files with the given suffix
    full_pattern = os.path.join(directory, f"{file_pattern}*.{suffix}")

    # Use glob to find all files matching the pattern
    matching_files = glob.glob(full_pattern)

    # Iterate over the matching files
    for file_path in matching_files:
        # Extract the file name from the full path
        file_name = os.path.basename(file_path)

        # Use mimetypes to guess the MIME type of the file
        mime_type, _ = mimetypes.guess_type(file_path)

        # Add the file name and MIME type to the dictionary
        file_mime_types[file_name] = mime_type

    return file_mime_types