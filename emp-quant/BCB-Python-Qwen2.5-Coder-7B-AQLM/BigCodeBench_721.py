
import os
import csv
from collections import Counter

def task_func(file_path):
    if not os.path.exists(file_path):
        return None
    
    most_common_word = None
    frequency = 0
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for word in row:
                word = word.strip()
                if word:
                    count = Counter([word])
                    if count[word] > frequency:
                        most_common_word = word
                        frequency = count[word]
    
    return (most_common_word, frequency) if most_common_word else None