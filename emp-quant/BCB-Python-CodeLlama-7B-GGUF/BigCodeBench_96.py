
import csv
from collections import Counter
import operator

def task_func(csv_file, csv_delimiter):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=csv_delimiter)
        words = [word for row in reader for word in row]
        counter = Counter(words)
        sorted_counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_counter