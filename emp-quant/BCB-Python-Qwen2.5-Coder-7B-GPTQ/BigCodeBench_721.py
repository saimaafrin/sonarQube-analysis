import os
import csv
from collections import Counter
def task_func(file_path):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return None
    
    word_counts = Counter()
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for word in row:
                word_counts[word] += 1
    
    if not word_counts:
        return None
    
    most_common_word, frequency = word_counts.most_common(1)[0]
    return (most_common_word, frequency)