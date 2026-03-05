import os
import csv
from collections import Counter
def task_func(file_path):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return None
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        words = []
        for row in reader:
            words.extend(row)
    
    word_counts = Counter(words)
    most_common_word, frequency = word_counts.most_common(1)[0] if word_counts else (None, 0)
    
    return (most_common_word, frequency)