
import os
import glob
import csv

def task_func(directory_path, file_extension='.csv'):
    # Initialize an empty dictionary to store the results
    result_dict = {}
    
    # Get a list of all files with the specified extension in the directory
    files = glob.glob(os.path.join(directory_path, '*' + file_extension))
    
    # Iterate over the list of files
    for file in files:
        # Get the filename without the extension
        filename = os.path.splitext(os.path.basename(file))[0]
        
        # Initialize an empty list to store the rows from the file
        rows = []
        
        # Open the file and read the rows
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
        
        # Add the filename and rows to the dictionary
        result_dict[filename] = rows
    
    # Return the dictionary
    return result_dict