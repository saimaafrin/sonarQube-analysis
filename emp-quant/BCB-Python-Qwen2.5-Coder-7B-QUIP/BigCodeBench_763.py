
import numpy as np
from collections import defaultdict
import json
import csv

# Constants
def task_func(input_file, output_file):
    # Read data from JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Initialize a dictionary to store results
    results = defaultdict(dict)

    # Iterate over each dictionary in the list
    for item in data:
        for key, value in item.items():
            # Initialize the result dictionary for the key if it doesn't exist
            if key not in results:
                results[key]['mean'] = []
                results[key]['median'] = []

            # Append the value to the list for the key
            results[key]['mean'].append(value)
            results[key]['median'].append(value)

    # Calculate mean and median for each key
    for key in results:
        results[key]['mean'] = np.mean(results[key]['mean'])
        results[key]['median'] = np.median(results[key]['median'])

    # Write the results to a CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Field', 'Mean', 'Median'])
        for key, value in results.items():
            writer.writerow([key, value['mean'], value['median']])

    return results