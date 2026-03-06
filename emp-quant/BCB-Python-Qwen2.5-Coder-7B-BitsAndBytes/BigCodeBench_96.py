
import csv
from collections import Counter
import operator

def task_func(csv_file, csv_delimiter):
    # Initialize a counter to keep track of word frequencies
    word_counter = Counter()
    
    # Open the CSV file and read its contents
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=csv_delimiter)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Split each row into words based on spaces
            words = ' '.join(row).split()
            
            # Update the word counter with the words from this row
            word_counter.update(words)
    
    # Get the most common words and their counts
    most_common_words = word_counter.most_common()
    
    return most_common_words