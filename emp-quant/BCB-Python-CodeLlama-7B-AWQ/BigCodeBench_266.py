import os
import os.path
import csv
import collections
FILE_NAME = 'file_sizes.csv'
def task_func(my_path):
    """
    Create a report on the file size in a directory and write it to a CSV file.
    """
    # Create a list to store the file sizes
    file_sizes = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(my_path):
        # Add the file sizes to the list
        for file in files:
            file_sizes.append(os.path.getsize(os.path.join(root, file)))

    # Write the file sizes to a CSV file
    with open(FILE_NAME, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Name', 'File Size'])
        for file_size in file_sizes:
            writer.writerow([file_size])

    # Return the path of the CSV file
    return os.path.join(os.getcwd(), FILE_NAME)