
import subprocess
import csv
import glob
import random
import os

def task_func(file):
    # Check if the file exists and is a CSV file
    if not os.path.exists(file) or not file.endswith('.csv'):
        return []

    # Split the CSV file into smaller files
    base_name = os.path.splitext(file)[0]
    split_files = []
    try:
        subprocess.run(['split', '-l', '1000', file, f'{base_name}_split_'], check=True)
        split_files = glob.glob(f'{base_name}_split_*')
    except subprocess.CalledProcessError:
        return []

    # Shuffle the rows in each split file
    for split_file in split_files:
        with open(split_file, mode='r') as infile, open('temp.csv', mode='w', newline='') as outfile:
            reader = csv.reader(infile)
            data = list(reader)
            random.shuffle(data)
            writer = csv.writer(outfile)
            writer.writerows(data)

        # Replace the original split file with the shuffled one
        os.remove(split_file)
        os.rename('temp.csv', split_file)

    return split_files