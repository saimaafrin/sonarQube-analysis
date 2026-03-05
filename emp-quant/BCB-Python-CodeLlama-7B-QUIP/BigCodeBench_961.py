
import os
import glob
from collections import Counter

def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    if not os.path.exists(directory):
        raise OSError("Directory does not exist")
    counter = Counter()
    for extension in extensions:
        counter[extension] = len(glob.glob(os.path.join(directory, "**", "*" + extension)))
    if not keep_zero:
        counter.pop(0)
    return counter