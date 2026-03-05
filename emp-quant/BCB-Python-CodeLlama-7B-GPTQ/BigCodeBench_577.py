import os
import pathlib
from hashlib import md5
import unicodedata
def task_func(directory):
    """
    Processes all files within the specified directory, normalizes their filenames to ASCII, calculates their MD5 hashes, and retrieves their sizes. It returns a dictionary where each key is the normalized file name and each value is another dictionary with the file's size and MD5 hash. This method is useful for file integrity checks and file organization tasks.
    """
    # Create a dictionary to store the results
    result_dict = {}

    # Iterate over all files in the directory
    for file in os.listdir(directory):
        # Get the full path of the file
        file_path = os.path.join(directory, file)

        # Get the file size in bytes
        file_size = os.path.getsize(file_path)

        # Get the MD5 hash of the file
        file_hash = md5(open(file_path, 'rb').read()).hexdigest()

        # Normalize the file name to ASCII
        file_name = unicodedata.normalize('NFKD', file).encode('ascii', 'ignore').decode('ascii')

        # Add the file's size and MD5 hash to the result dictionary
        result_dict[file_name] = {'Size': file_size, 'MD5 Hash': file_hash}

    return result_dict
directory = 'path/to/directory'