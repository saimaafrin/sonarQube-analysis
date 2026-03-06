
import re
import os
from pathlib import Path
import csv

def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:
    """
    Processes CSV files in a directory based on a specified pattern and creates new files with altered names while preserving the content.

    Args:
        directory (str): The directory containing the CSV files to process.
        pattern (str, optional): The pattern to use for matching CSV files. Defaults to r'^(.*?)-\d+\.csv$'.

    Returns:
        list: A list of strings, where each string is the filename of a new CSV file created by the function.
    """
    new_files = []

    # Get a list of all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if re.match(pattern, f)]

    # Process each CSV file
    for csv_file in csv_files:
        # Open the CSV file
        with open(os.path.join(directory, csv_file), 'r') as f:
            # Create a new CSV file with the same content
            new_file = csv.reader(f)
            new_filename = re.sub(r'\d+', '', csv_file)
            new_file.to_csv(os.path.join(directory, new_filename), index=False)
            new_files.append(new_filename)

    return new_files