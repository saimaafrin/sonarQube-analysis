
import subprocess
import csv
import glob
import random
import os

def task_func(file):
    # Check if the file exists and is a CSV file
    if not os.path.exists(file) or not file.endswith('.csv'):
        return []

    # Get the base name of the file without the extension
    base_name = os.path.splitext(file)[0]

    # Use the 'split' command to divide the CSV file into smaller files
    subprocess.run(['split', '-l', '1000', file, base_name], check=True)

    # Get the list of split files
    split_files = glob.glob(f"{base_name}*")

    # Shuffle the lines in each split file
    for split_file in split_files:
        with open(split_file, 'r') as f:
            lines = f.readlines()
        random.shuffle(lines)
        with open(split_file, 'w') as f:
            f.writelines(lines)

    # Return the list of split file paths
    return split_files