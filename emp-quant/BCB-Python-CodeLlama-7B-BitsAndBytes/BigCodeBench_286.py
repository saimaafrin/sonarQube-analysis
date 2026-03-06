
from collections import Counter
import os
import csv

# Constants
FILE_DIR = './yourdictfiles/'

def task_func(output_file, test_directory):
    # Create a Counter object to keep track of the word counts
    word_counts = Counter()

    # Loop through all the files in the directory
    for filename in os.listdir(test_directory):
        # Open the file and read its contents
        with open(os.path.join(test_directory, filename), 'r') as f:
            contents = f.read()

        # Split the contents into words and update the Counter object
        for word in contents.split():
            word_counts[word] += 1

    # Write the word counts to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        for word, count in word_counts.items():
            writer.writerow([word, count])

    # Return the total number of words
    return sum(word_counts.values())