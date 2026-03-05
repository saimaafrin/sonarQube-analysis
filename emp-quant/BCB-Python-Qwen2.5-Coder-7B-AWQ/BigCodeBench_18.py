import subprocess
import csv
import glob
import random
import os
def task_func(file):
    # Check if the file exists and is a CSV file
    if not os.path.exists(file) or not file.endswith('.csv'):
        return []

    # Split the CSV file into smaller files using the 'split' command
    split_files = []
    try:
        subprocess.run(['split', '-l', '1000', file, 'split_'], check=True)
        split_files = glob.glob('split_*')
    except subprocess.CalledProcessError:
        return []

    # Shuffle the rows in each of the resulting files
    for split_file in split_files:
        with open(split_file, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)

        random.shuffle(rows)

        with open(split_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

    return split_files