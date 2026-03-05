
import os
import os.path
import csv
import collections

# Constants
FILE_NAME = 'file_sizes.csv'

def task_func(my_path):
    # Create the CSV file
    with open(FILE_NAME, 'w', newline='') as csvfile:
        fieldnames = ['file', 'size']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()

    # Walk the directory and get the file sizes
    for root, dirs, files in os.walk(my_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            writer.writerow({'file': file, 'size': file_size})

    # Return the path of the CSV file
    return FILE_NAME