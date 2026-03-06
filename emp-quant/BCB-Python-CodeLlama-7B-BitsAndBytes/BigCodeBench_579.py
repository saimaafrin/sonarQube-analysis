
import unicodedata
import csv
from collections import Counter
import matplotlib.pyplot as plt

def task_func(csv_file):
    # Open the CSV file and read it into a list of rows
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Normalize the text in each row to ASCII
    normalized_rows = []
    for row in rows:
        normalized_row = []
        for cell in row:
            normalized_cell = unicodedata.normalize('NFKD', cell).encode('ascii', 'ignore')
            normalized_row.append(normalized_cell)
        normalized_rows.append(normalized_row)

    # Count the words in each row and create a Counter object
    word_counts = Counter()
    for row in normalized_rows:
        for cell in row:
            words = cell.split()
            for word in words:
                word_counts[word] += 1

    # Create a bar plot of the 10 most common words
    plt.bar(range(10), word_counts.most_common(10))
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.title('Most Common Words in the CSV File')
    plt.show()

    # Return the list of tuples containing the 10 most common words and their frequencies
    return word_counts.most_common(10)