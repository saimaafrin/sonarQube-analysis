import os
import pathlib
from hashlib import md5
import unicodedata
def task_func(directory):
    """
    Processes all files within the specified directory, normalizes their filenames to ASCII, calculates their MD5 hashes, and retrieves their sizes. It returns a dictionary where each key is the normalized file name and each value is another dictionary with the file's size and MD5 hash. This method is useful for file integrity checks and file organization tasks.
    """
    # Create a dictionary to store the results
    results = {}

    # Iterate over all files in the directory
    for file in os.listdir(directory):
        # Get the full path of the file
        file_path = os.path.join(directory, file)

        # Normalize the filename to ASCII
        normalized_filename = unicodedata.normalize('NFKD', file).encode('ascii', 'ignore').decode('ascii')

        # Calculate the MD5 hash of the file
        with open(file_path, 'rb') as f:
            md5_hash = md5(f.read()).hexdigest()

        # Get the size of the file
        size = os.path.getsize(file_path)

        # Add the result to the dictionary
        results[normalized_filename] = {'Size': size, 'MD5 Hash': md5_hash}

    return results
directory = 'path/to/directory'