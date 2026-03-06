
import os
import glob
from collections import Counter

def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    if not os.path.exists(directory):
        raise OSError(f"The directory {directory} does not exist.")
    
    file_counts = Counter()
    
    for ext in extensions:
        pattern = os.path.join(directory, "**", f"*{ext}")
        files = glob.glob(pattern, recursive=True)
        file_counts[ext] = len(files)
    
    if not keep_zero:
        file_counts = {ext: count for ext, count in file_counts.items() if count > 0}
    
    return file_counts