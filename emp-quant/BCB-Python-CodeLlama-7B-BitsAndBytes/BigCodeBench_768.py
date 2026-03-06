
import re
import os
import glob

def task_func(dir_path):
    if not os.path.exists(dir_path):
        raise ValueError("Directory does not exist")

    file_paths = glob.glob(os.path.join(dir_path, "**", "*.txt"), recursive=True)
    error_counts = {}

    for file_path in file_paths:
        with open(file_path, "r") as file:
            text = file.read()
            error_counts[file_path] = len(re.findall(r"error", text, re.IGNORECASE))

    return error_counts