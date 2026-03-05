
import os
import csv
from collections import Counter

def task_func(file_path):
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        words = [word for row in reader for word in row]

    counter = Counter(words)
    most_common_word, most_common_count = counter.most_common(1)[0]

    return most_common_word, most_common_count