
from collections import Counter
import os
import csv

# Constants
FILE_DIR = './yourdictfiles/'

def task_func(output_file, test_directory):
    # Check if the input directory is valid
    if not os.path.isdir(test_directory):
        return 0

    # Create a list to store the words and their counts
    word_counts = Counter()

    # Iterate over the files in the directory
    for filename in os.listdir(test_directory):
        # Check if the file is a .txt file
        if not filename.endswith('.txt'):
            continue

        # Open the file and read its contents
        with open(os.path.join(test_directory, filename), 'r') as f:
            contents = f.read()

        # Split the contents into words and add them to the counter
        for word in contents.split():
            word_counts[word] += 1

    # Write the word counts to a CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Word', 'Count'])
        for word, count in word_counts.items():
            writer.writerow([word, count])

    # Return the total number of words
    return sum(word_counts.values())