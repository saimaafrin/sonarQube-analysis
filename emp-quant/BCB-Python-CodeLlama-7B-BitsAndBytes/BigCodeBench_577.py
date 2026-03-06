
import os
import pathlib
from hashlib import md5
import unicodedata

def task_func(directory):
    file_dict = {}
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_name = unicodedata.normalize('NFKD', file).encode('ascii', 'ignore').decode()
            file_size = os.path.getsize(file_path)
            file_hash = md5(open(file_path, 'rb').read()).hexdigest()
            file_dict[file_name] = {'Size': file_size, 'MD5 Hash': file_hash}
    return file_dict