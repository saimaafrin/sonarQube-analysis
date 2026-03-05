import os
import re
import json
import glob
def task_func(directory_path: str) -> list:
    """
    Protect all double quotes in all JSON files in the specified directory by prepending them with a double backslash.
    """
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory {directory_path} does not exist.")

    processed_files = []
    for file in glob.glob(os.path.join(directory_path, "*.json")):
        with open(file, "r") as f:
            data = json.load(f)
        data = json.dumps(data, ensure_ascii=False)
        data = re.sub(r'"', '\\"', data)
        with open(file, "w") as f:
            f.write(data)
        processed_files.append(file)

    return processed_files
directory_path = "path/to/directory"