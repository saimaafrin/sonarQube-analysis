import csv
from collections import Counter
import operator
def task_func(csv_file, csv_delimiter):
    """
    Reads a CSV file and counts the most common words in the file.
    This function opens the specified CSV file using the provided delimiter,
    reads its contents, and counts the frequency of each word.
    It returns a list of tuples, each containing a word and its frequency,
    sorted by frequency in descending order.
    """
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=csv_delimiter)
        words = [word for row in reader for word in row]
        counter = Counter(words)
        return sorted(counter.items(), key=operator.itemgetter(1), reverse=True)