
import csv
import os

def task_func(data, file_path, headers):
    if file_path is None:
        raise ValueError("file_path cannot be None")
    
    # Determine the absolute path
    absolute_path = os.path.abspath(file_path)
    
    # Write the data to the CSV file
    with open(absolute_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the headers
        writer.writerow(headers)
        # Write the data rows
        for row in data:
            # Fill missing elements with None
            writer.writerow(row + [None] * (len(headers) - len(row)))
    
    return absolute_path