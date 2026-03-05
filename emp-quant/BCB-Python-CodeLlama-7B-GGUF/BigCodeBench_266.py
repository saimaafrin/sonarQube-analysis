
import os
import os.path
import csv
import collections

# Constants
FILE_NAME = 'file_sizes.csv'

def task_func(my_path):
    # Create a dictionary to store the file sizes
    file_sizes = collections.defaultdict(int)

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(my_path):
        # Add the file sizes to the dictionary
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_sizes[file] = file_size

    # Write the dictionary to a CSV file
    with open(FILE_NAME, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file, size in file_sizes.items():
            writer.writerow([file, size])

    # Return the path of the CSV file
    return FILE_NAME