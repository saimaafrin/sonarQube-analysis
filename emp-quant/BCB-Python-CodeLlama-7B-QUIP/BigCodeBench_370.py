
import os
import re
import json
import glob

def task_func(directory_path: str) -> list:
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory {directory_path} does not exist.")
    file_paths = glob.glob(os.path.join(directory_path, "*.json"))
    processed_files = []
    for file_path in file_paths:
        with open(file_path, "r") as f:
            content = f.read()
        # Replace double quotes with double backslashes
        content = re.sub(r'"', r'\\"', content)
        with open(file_path, "w") as f:
            f.write(content)
        processed_files.append(file_path)
    return processed_files