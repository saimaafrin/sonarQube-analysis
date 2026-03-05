
import os
import pathlib
from hashlib import md5
import unicodedata

def normalize_filename(filename):
    """Normalize the filename to ASCII."""
    return unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')

def task_func(directory):
    """
    Processes all files within the specified directory, normalizes their filenames to ASCII,
    calculates their MD5 hashes, and retrieves their sizes. Returns a dictionary where each key
    is the normalized file name and each value is another dictionary with the file's size and MD5 hash.
    
    :param directory: str, the path to the directory containing the files.
    :return: dict, a dictionary where each key is a normalized file name, and the value is a dictionary
             containing the 'Size' (in bytes) and 'MD5 Hash' of the file.
    """
    file_info = {}
    for file_path in pathlib.Path(directory).iterdir():
        if file_path.is_file():
            normalized_name = normalize_filename(file_path.name)
            file_size = file_path.stat().st_size
            file_hash = md5(file_path.read_bytes()).hexdigest()
            file_info[normalized_name] = {'Size': file_size, 'MD5 Hash': file_hash}
    return file_info