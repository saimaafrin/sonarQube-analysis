
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
            file_sizes[file] += os.path.getsize(os.path.join(root, file))

    # Write the dictionary to a CSV file
    with open(FILE_NAME, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file, size in file_sizes.items():
            writer.writerow([file, size])

    # Return the path of the CSV file
    return FILE_NAME

# Call the function with the path of the directory to analyze
path = '/path/to/directory'
csv_file = task_func(path)
print(f'File sizes written to {csv_file}')