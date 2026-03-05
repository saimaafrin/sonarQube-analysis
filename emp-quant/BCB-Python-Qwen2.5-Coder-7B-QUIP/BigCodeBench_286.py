
from collections import Counter
import os
import csv
# Constants
FILE_DIR = './yourdictfiles/'

def task_func(output_file, test_directory):
    # Check if the directory exists
    if not os.path.exists(test_directory):
        return 0

    # Initialize a Counter to keep track of word counts
    word_counter = Counter()

    # List all files in the directory
    files = os.listdir(test_directory)

    # Iterate over the files and count words
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(test_directory, file)
            with open(file_path, 'r') as f:
                word_counter.update(f.read().split())

    # Write the counts to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        writer.writerows(word_counter.items())

    # Return the total number of words
    return sum(word_counter.values())