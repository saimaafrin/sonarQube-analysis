
import re
import os
import glob

def task_func(dir_path):
    if not os.path.exists(dir_path):
        raise ValueError("Directory does not exist")

    file_paths = glob.glob(os.path.join(dir_path, "*.txt"))
    error_counts = {}

    for file_path in file_paths:
        with open(file_path, "r") as f:
            text = f.read()
            error_count = len(re.findall(r"\berror\b", text, re.IGNORECASE))
            error_counts[file_path] = error_count

    return error_counts