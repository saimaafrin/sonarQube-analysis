import csv
import os
def task_func(data, file_path, headers):
    if file_path is None:
        raise ValueError("file_path cannot be None")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in data:
            # Fill missing elements with None
            row += [None] * (len(headers) - len(row))
            writer.writerow(row)
    
    return os.path.abspath(file_path)