
import os
import glob
from collections import Counter

def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    if not os.path.exists(directory):
        raise OSError(f"Directory {directory} does not exist")
    
    file_counts = Counter()
    for ext in extensions:
        pattern = os.path.join(directory, f"*{ext}")
        file_counts[ext] = len(glob.glob(pattern))
    
    if not keep_zero:
        file_counts = Counter({k: v for k, v in file_counts.items() if v != 0})
    
    return file_counts