
import os
import os.path
import csv
import collections

# Constants
FILE_NAME = 'file_sizes.csv'

def task_func(my_path):
    # Dictionary to store file sizes
    file_sizes = collections.defaultdict(int)
    
    # Walk through the directory
    for root, dirs, files in os.walk(my_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Get the size of the file
                size = os.path.getsize(file_path)
                file_sizes[file_path] = size
            except Exception as e:
                print(f"Error accessing {file_path}: {e}")
    
    # Write the file sizes to a CSV file
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['File Path', 'Size (bytes)'])
        for file_path, size in file_sizes.items():
            writer.writerow([file_path, size])
    
    # Return the path of the CSV file
    return FILE_NAME