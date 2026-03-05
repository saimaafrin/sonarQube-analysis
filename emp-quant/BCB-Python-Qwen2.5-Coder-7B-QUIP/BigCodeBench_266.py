
import os
import os.path
import csv
import collections
# Constants
FILE_NAME = 'file_sizes.csv'

def task_func(my_path):
    # Create a dictionary to hold the file sizes
    file_sizes = collections.defaultdict(int)

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(my_path):
        for file in files:
            # Get the full path of the file
            full_path = os.path.join(root, file)
            # Add the file size to the dictionary
            file_sizes[full_path] += os.path.getsize(full_path)

    # Write the file sizes to a CSV file
    with open(FILE_NAME, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File', 'Size'])
        for file, size in file_sizes.items():
            writer.writerow([file, size])

    # Return the path of the CSV file
    return FILE_NAME