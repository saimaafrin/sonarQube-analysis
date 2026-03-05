
import os
import csv
from collections import Counter

def task_func(file_path):
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row[0] for row in reader]

    if not data:
        return None

    word_counts = Counter(data)
    most_common = word_counts.most_common(1)[0]

    return most_common