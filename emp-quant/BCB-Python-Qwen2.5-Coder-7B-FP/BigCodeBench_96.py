import csv
from collections import Counter
import operator
def task_func(csv_file, csv_delimiter):
    word_counts = Counter()
    
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=csv_delimiter)
        for row in reader:
            for cell in row:
                words = cell.split()
                word_counts.update(words)
    
    sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_word_counts
csv_file = 'example.csv'
csv_delimiter = ','