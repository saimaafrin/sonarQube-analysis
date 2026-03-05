import csv
from collections import Counter
import operator
def task_func(csv_file, csv_delimiter):
    # Initialize a Counter object to store word frequencies
    word_counter = Counter()
    
    # Open the CSV file and read its contents
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=csv_delimiter)
        for row in reader:
            # Count each word in the row
            for word in row:
                word_counter[word] += 1
    
    # Sort the words by frequency in descending order
    sorted_words = sorted(word_counter.items(), key=operator.itemgetter(1), reverse=True)
    
    return sorted_words