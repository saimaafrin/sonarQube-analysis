
import os
import csv
from collections import Counter

def task_func(file_path):
    if not os.path.exists(file_path):
        return None
    
    word_count = Counter()
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for word in row:
                word_count[word] += 1
    
    if not word_count:
        return None
    
    most_common_word, frequency = word_count.most_common(1)[0]
    return (most_common_word, frequency)