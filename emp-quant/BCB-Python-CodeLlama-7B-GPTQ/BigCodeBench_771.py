import re
import os
from pathlib import Path
import csv
def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:
    """
    Processes CSV files in a directory based on a specified pattern and creates new files with altered names while preserving the content.

    Args:
        directory (str): The directory containing the CSV files.
        pattern (str, optional): The pattern to match the filenames against. Defaults to r'^(.*?)-\d+\.csv$'.

    Returns:
        new_files (list): A list of strings, where each string is the filename of a new CSV file created by the function.
    """
    new_files = []
    for file in os.listdir(directory):
        if re.match(pattern, file):
            with open(os.path.join(directory, file), 'r') as f:
                reader = csv.reader(f)
                new_file = re.sub(r'\d+', '', file) + '.csv'
                with open(os.path.join(directory, new_file), 'w', newline='') as g:
                    writer = csv.writer(g)
                    for row in reader:
                        writer.writerow(row)
                new_files.append(new_file)
    return new_files
directory = 'path/to/directory'
pattern = r'^(.*?)-\d+\.csv$'