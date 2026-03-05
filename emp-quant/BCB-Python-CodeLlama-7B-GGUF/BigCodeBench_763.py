
import numpy as np
from collections import defaultdict
import json
import csv

# Constants
INPUT_FILE = 'input.json'
OUTPUT_FILE = 'output.csv'

def task_func(input_file, output_file):
    # Read JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Calculate mean and median for each key
    means = defaultdict(list)
    medians = defaultdict(list)
    for d in data:
        for k, v in d.items():
            means[k].append(np.mean(v))
            medians[k].append(np.median(v))

    # Write results to CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for k, v in means.items():
            writer.writerow([k, np.mean(v)])
        for k, v in medians.items():
            writer.writerow([k, np.median(v)])