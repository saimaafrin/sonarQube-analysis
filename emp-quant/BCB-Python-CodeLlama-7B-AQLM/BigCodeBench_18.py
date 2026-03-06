import subprocess
import csv
import glob
import random
import os
def task_func(file):
    """
    Divide a CSV file into several smaller files and shuffle the lines in each file.
    
    This function takes a CSV file path as input, divides it into smaller files using 
    the shell 'split' command, and shuffles the rows in each of the resulting files.
    The output files are named with a 'split_' prefix.

    Parameters:
    - file (str): The path to the CSV file.

    Returns:
    - list: The paths to the split files. Returns an empty list if the file does not exist, is not a CSV file, or if an error occurs during processing.
    
    Requirements:
    - subprocess
    - csv
    - glob
    - random
    - os

    Example:
    >>> task_func('/path/to/file.csv')
    ['/path/to/split_00', '/path/to/split_01', ...]
    """
    if not os.path.exists(file):
        return []
    if not file.endswith('.csv'):
        return []
    try:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            lines = list(reader)
    except:
        return []
    if len(lines) == 0:
        return []
    try:
        subprocess.run(['split', '-l', '1000', file, 'split_'], check=True)
    except:
        return []
    files = glob.glob('split_*')
    for file in files:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            lines = list(reader)
        random.shuffle(lines)
        with open(file, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(lines)
    return files