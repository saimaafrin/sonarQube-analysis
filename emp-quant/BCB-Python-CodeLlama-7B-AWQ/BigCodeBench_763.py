import numpy as np
from collections import defaultdict
import json
import csv
def task_func(input_file, output_file):
    """
    Read a list of dictionaries from a JSON file, calculate the mean and median for each key, and write the results to a CSV file.
    """
    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Initialize the output CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['key', 'mean', 'median'])

    # Calculate the mean and median for each key
    for d in data:
        for k, v in d.items():
            if isinstance(v, list):
                mean = np.mean(v)
                median = np.median(v)
                writer.writerow([k, mean, median])