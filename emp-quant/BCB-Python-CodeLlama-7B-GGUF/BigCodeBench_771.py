
import re
import os
from pathlib import Path
import csv

def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:
    """
    Processes CSV files in a directory based on a specified pattern and creates new files with altered names while preserving the content.

    Args:
        directory (str): The directory containing the CSV files to process.
        pattern (str, optional): The pattern to match the filenames against. Defaults to r'^(.*?)-\d+\.csv$'.

    Returns:
        list: A list of strings, where each string is the filename of a new CSV file created by the function.
    """
    new_files = []

    # Get a list of all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    # Iterate over the CSV files and process them
    for csv_file in csv_files:
        # Open the CSV file
        with open(os.path.join(directory, csv_file), 'r') as f:
            # Create a new CSV file with the same content
            new_file = re.sub(pattern, r'\1-new.csv', csv_file)
            with open(os.path.join(directory, new_file), 'w', newline='') as new_f:
                # Write the content of the CSV file to the new file
                writer = csv.writer(new_f)
                reader = csv.reader(f)
                for row in reader:
                    writer.writerow(row)

            # Add the new file to the list of new files
            new_files.append(new_file)

    return new_files