
from collections import Counter
import os
import csv

# Constants
FILE_DIR = './yourdictfiles/'

def task_func(output_file, test_directory):
    # Check if the input is valid
    if not os.path.exists(test_directory):
        raise ValueError("Invalid input directory")

    # Initialize the counter
    counter = Counter()

    # Loop through all files in the directory
    for file_name in os.listdir(test_directory):
        # Get the full file path
        file_path = os.path.join(test_directory, file_name)

        # Check if the file is a .txt file
        if file_name.endswith('.txt'):
            # Open the file and read it line by line
            with open(file_path, 'r') as file:
                # Loop through each line in the file
                for line in file:
                    # Add the words in the line to the counter
                    counter.update(line.split())

    # Write the counter to the output file
    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'Count'])
        for word, count in counter.items():
            writer.writerow([word, count])

    # Return the total number of words
    return sum(counter.values())