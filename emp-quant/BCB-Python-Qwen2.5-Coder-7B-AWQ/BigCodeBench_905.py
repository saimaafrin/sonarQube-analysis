import os
import glob
import csv
def task_func(directory_path, file_extension='.csv'):
    data = {}
    # Find all files with the specified extension in the directory
    files = glob.glob(os.path.join(directory_path, f'*{file_extension}'))
    
    for file_path in files:
        # Extract the filename without the extension
        filename = os.path.splitext(os.path.basename(file_path))[0]
        # Initialize an empty list to store rows
        rows = []
        
        # Open the file and read rows
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        
        # Add the rows to the dictionary with the filename as the key
        data[filename] = rows
    
    return data