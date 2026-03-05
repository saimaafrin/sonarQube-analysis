
import os
import pathlib
from hashlib import md5
import unicodedata

def task_func(directory):
    file_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_md5 = md5(open(file_path, 'rb').read()).hexdigest()
            file_dict[file_name] = {'Size': file_size, 'MD5 Hash': file_md5}
    return file_dict