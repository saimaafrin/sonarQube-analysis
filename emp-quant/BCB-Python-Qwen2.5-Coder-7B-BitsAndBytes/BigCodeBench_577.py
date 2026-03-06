
import os
import pathlib
from hashlib import md5
import unicodedata

def normalize_filename(filename):
    """Normalize the filename to ASCII."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', filename)
        if unicodedata.category(c) != 'Mn'
    )

def calculate_md5(file_path):
    """Calculate the MD5 hash of a file."""
    hasher = md5()
    with open(file_path, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def task_func(directory):
    """
    Processes all files within the specified directory, normalizes their filenames to ASCII,
    calculates their MD5 hashes, and retrieves their sizes. Returns a dictionary where each key
    is the normalized file name and each value is another dictionary with the file's size and MD5 hash.

    :param directory: str, the path to the directory containing the files.
    :return: dict, a dictionary where each key is a normalized file name, and the value is a dictionary
             containing the 'Size' (in bytes) and 'MD5 Hash' of the file.
    """
    result = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            normalized_file_name = normalize_filename(file)
            file_size = os.path.getsize(file_path)
            file_md5 = calculate_md5(file_path)
            result[normalized_file_name] = {'Size': file_size, 'MD5 Hash': file_md5}
    return result