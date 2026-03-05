
import os
import glob
from collections import Counter

def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    if not os.path.exists(directory):
        raise OSError(f"The specified directory {directory} does not exist.")
    
    file_counts = Counter()
    
    for ext in extensions:
        pattern = os.path.join(directory, f"*{ext}")
        for file_path in glob.glob(pattern, recursive=True):
            if os.path.isfile(file_path):
                file_counts[ext] += 1
    
    if not keep_zero:
        file_counts = {ext: count for ext, count in file_counts.items() if count > 0}
    
    return file_counts