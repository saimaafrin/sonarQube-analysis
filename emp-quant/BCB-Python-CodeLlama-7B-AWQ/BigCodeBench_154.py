import re
import os
import glob
import mimetypes
def task_func(directory, file_pattern, suffix):
    """
    Scans a specified directory for files matching a given pattern and with a certain suffix, then determines their file types.
    The function returns a dictionary with file names as keys and their corresponding MIME types as values.
    """
    file_names = []
    mime_types = {}
    for file in glob.glob(os.path.join(directory, file_pattern)):
        if file.endswith(suffix):
            file_names.append(file)
            mime_types[file] = mimetypes.guess_type(file)[0]
    return mime_types
directory = "."
file_pattern = "*.txt"
suffix = ".txt"