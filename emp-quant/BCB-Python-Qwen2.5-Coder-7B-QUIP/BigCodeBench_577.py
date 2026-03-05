
import os
import pathlib
from hashlib import md5
import unicodedata

def task_func(directory):
    result = {}
    for file_name in os.listdir(directory):
        normalized_name = unicodedata.normalize('NFKD', file_name).encode('ascii', 'ignore').decode()
        normalized_name = "".join(c for c in normalized_name if c.isalnum() or c in "_.-")
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            file_hash = md5(open(file_path, 'rb').read()).hexdigest()
            result[normalized_name] = {'Size': file_size, 'MD5 Hash': file_hash}
    return result