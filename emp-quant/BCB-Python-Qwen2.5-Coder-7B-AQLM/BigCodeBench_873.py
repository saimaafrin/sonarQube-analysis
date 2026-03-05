
import csv
import os

def task_func(data, file_path, headers):
    if file_path is None:
        raise ValueError("file_path cannot be None")
    
    # Determine the number of columns based on the headers
    num_columns = len(headers)
    
    # Pad each tuple with None if it has fewer elements than the number of headers
    padded_data = [tuple(row + [None] * (num_columns - len(row))) for row in data]
    
    # Write the data to the CSV file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(padded_data)
    
    # Return the absolute path of the saved CSV file
    return os.path.abspath(file_path)