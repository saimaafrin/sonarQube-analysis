import os
import pathlib
from hashlib import md5
import unicodedata
def normalize_filename(filename):
    """Normalize the filename to ASCII."""
    return unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')
def calculate_md5(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
def task_func(directory):
    """
    Processes all files within the specified directory, normalizes their filenames to ASCII,
    calculates their MD5 hashes, and retrieves their sizes. Returns a dictionary where each key
    is the normalized file name and each value is another dictionary with the file's size and MD5 hash.
    """
    result = {}
    for file_path in pathlib.Path(directory).iterdir():
        if file_path.is_file():
            normalized_name = normalize_filename(file_path.name)
            file_size = file_path.stat().st_size
            file_md5 = calculate_md5(file_path)
            result[normalized_name] = {'Size': file_size, 'MD5 Hash': file_md5}
    return result