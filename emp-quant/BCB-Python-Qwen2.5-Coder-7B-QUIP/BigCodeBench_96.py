
import csv
from collections import Counter
import operator

def task_func(csv_file, csv_delimiter):
    # Open the CSV file and read its contents
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=csv_delimiter)
        # Read all rows and split them into words
        words = []
        for row in reader:
            words.extend(row)
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Return the list of tuples with words and their counts, sorted by count
    return word_counts.most_common()