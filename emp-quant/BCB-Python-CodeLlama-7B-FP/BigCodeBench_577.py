import os
import pathlib
from hashlib import md5
import unicodedata
def task_func(directory):
    """
    Processes all files within the specified directory, normalizes their filenames to ASCII, calculates their MD5 hashes, and retrieves their sizes.
    It returns a dictionary where each key is the normalized file name and each value is another dictionary with the file's size and MD5 hash.
    This method is useful for file integrity checks and file organization tasks.
    """
    file_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = unicodedata.normalize('NFKD', file).encode('ascii', 'ignore').decode('ascii')
            file_size = os.path.getsize(file_path)
            file_hash = md5(open(file_path, 'rb').read()).hexdigest()
            file_dict[file_name] = {'Size': file_size, 'MD5 Hash': file_hash}
    return file_dict
directory = 'path/to/directory'