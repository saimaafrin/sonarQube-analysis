import os
import glob
import csv
def task_func(directory_path, file_extension='.csv'):
    data = {}
    # Use glob to find all files with the specified extension in the directory
    for file_path in glob.glob(os.path.join(directory_path, f'*{file_extension}')):
        # Extract the filename without the extension
        filename = os.path.splitext(os.path.basename(file_path))[0]
        # Initialize an empty list to store rows from the file
        rows = []
        # Open the file and read rows using csv.reader
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        # Add the filename and its rows to the dictionary
        data[filename] = rows
    return data