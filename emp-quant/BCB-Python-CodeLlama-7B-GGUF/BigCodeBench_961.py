
import os
import glob
from collections import Counter

def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    if not os.path.exists(directory):
        raise OSError("Directory does not exist")

    file_counts = Counter()
    for ext in extensions:
        file_counts[ext] = len(glob.glob(os.path.join(directory, "**", f"*{ext}"), recursive=True))

    if not keep_zero:
        file_counts = {ext: count for ext, count in file_counts.items() if count > 0}

    return file_counts