
import csv
from collections import Counter
import operator

def task_func(csv_file, csv_delimiter):
    # Open the CSV file and read its contents
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=csv_delimiter)
        contents = [row for row in reader]

    # Flatten the list of lists into a single list of words
    words = [word for row in contents for word in row]

    # Count the frequency of each word
    counter = Counter(words)

    # Sort the counter by frequency in descending order
    sorted_counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

    # Return the list of tuples
    return sorted_counter