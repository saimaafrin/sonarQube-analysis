
import subprocess
import csv
import glob
import random
import os

def task_func(file):
    # Check if the file exists and is a CSV file
    if not os.path.isfile(file) or not file.endswith('.csv'):
        return []

    # Split the CSV file into smaller files
    split_files = []
    try:
        subprocess.run(['split', '-l', '1000', file, 'split_'], check=True)
        split_files = glob.glob('split_*')
    except subprocess.CalledProcessError:
        return []

    # Shuffle the lines in each split file
    for split_file in split_files:
        with open(split_file, 'r') as f:
            lines = f.readlines()
        random.shuffle(lines)
        with open(split_file, 'w') as f:
            f.writelines(lines)

    return split_files