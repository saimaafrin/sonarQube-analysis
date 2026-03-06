
import csv
import os

def task_func(data, file_path, headers):
    if file_path is None:
        raise ValueError("File path cannot be None")
    
    # Determine the directory where the file will be saved
    directory = os.path.dirname(file_path)
    
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Open the file in write mode
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the headers
        writer.writerow(headers)
        
        # Write the data rows
        for row in data:
            # Fill missing values with None
            padded_row = row + [None] * (len(headers) - len(row))
            writer.writerow(padded_row)
    
    return os.path.abspath(file_path)