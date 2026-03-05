
import re
import os
import shutil
from datetime import datetime

def task_func(directory):
    files = os.listdir(directory)
    files_by_category = {}
    for file in files:
        match = re.search(r'\[.*\]', file)
        if match:
            category = match.group(0)
            files_by_category.setdefault(category, [])
            files_by_category[category].append(file)
    for category, files in files_by_category.items():
        for file in files:
            shutil.move(os.path.join(directory, file), os.path.join(directory, category, file))
    return directory, files_by_category