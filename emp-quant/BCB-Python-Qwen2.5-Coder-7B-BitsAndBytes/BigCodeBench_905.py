
import os
import glob
import csv

def task_func(directory_path, file_extension='.csv'):
    """
    Reads all files with the specified extension in the given directory.
    
    Parameters:
    directory_path (str): The path to the directory containing the files.
    file_extension (str): The file extension to filter the files (default is '.csv').
    
    Returns:
    dict: A dictionary where each key is the filename (without extension) and the value is a list of rows from the file.
    """
    data = {}
    
    # Construct the pattern to match files with the specified extension
    pattern = os.path.join(directory_path, f'*{file_extension}')
    
    # Find all files matching the pattern
    files = glob.glob(pattern)
    
    for file_path in files:
        # Extract the filename without the extension
        filename_without_ext = os.path.splitext(os.path.basename(file_path))[0]
        
        # Read the file and store its content in the dictionary
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            data[filename_without_ext] = [row for row in reader]
    
    return data