
import re
import os
import glob

def task_func(dir_path: str) -> list:
    file_names = glob.glob(dir_path + "/*")
    new_file_names = []
    for file_name in file_names:
        new_file_name = re.sub(r"[^\w\.]+", "", file_name)
        new_file_names.append(new_file_name)
    return new_file_names