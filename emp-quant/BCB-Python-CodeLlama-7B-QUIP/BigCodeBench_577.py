
import os
import pathlib
from hashlib import md5
import unicodedata

def task_func(directory):
    files = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        file_size = os.path.getsize(file_path)
        file_md5 = md5(file_path)
        file_name = unicodedata.normalize("NFKD", file).encode("ascii", "ignore").decode("utf-8")
        files.append({file_name: {"Size": file_size, "MD5 Hash": file_md5}})
    return files