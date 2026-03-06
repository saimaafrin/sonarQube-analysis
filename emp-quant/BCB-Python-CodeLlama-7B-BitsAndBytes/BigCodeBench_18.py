
import subprocess
import csv
import glob
import random
import os

def task_func(file):
    # Check if the file exists and is a CSV file
    if not os.path.exists(file) or not file.endswith('.csv'):
        return []

    # Split the file into smaller files using the shell 'split' command
    split_cmd = 'split -l 1000 {} split_'.format(file)
    subprocess.run(split_cmd, shell=True)

    # Shuffle the rows in each of the resulting files
    for filename in glob.glob('split_*'):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            random.shuffle(rows)
            with open(filename, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(rows)

    # Return the paths to the split files
    return glob.glob('split_*')