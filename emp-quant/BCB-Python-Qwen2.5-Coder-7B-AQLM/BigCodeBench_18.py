
import subprocess
import csv
import glob
import random
import os

def task_func(file):
    # Check if the file exists and is a CSV file
    if not os.path.isfile(file) or not file.endswith('.csv'):
        return []

    # Split the CSV file into smaller files using the 'split' command
    split_files = []
    split_prefix = 'split_'
    split_command = f"split -l 1000 {file} {split_prefix}"
    subprocess.run(split_command, shell=True, check=True)

    # Shuffle the rows in each split file
    for split_file in glob.glob(f"{split_prefix}*"):
        with open(split_file, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)

        random.shuffle(rows)

        with open(split_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        split_files.append(split_file)

    return split_files