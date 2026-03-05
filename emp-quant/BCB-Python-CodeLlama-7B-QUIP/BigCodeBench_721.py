
import os
import csv
from collections import Counter

def task_func(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        words = [word for line in reader for word in line.split()]
        counter = Counter(words)
        most_common = counter.most_common(1)[0]
        return most_common[0], most_common[1]