import numpy as np
from collections import defaultdict
import json
import csv
def task_func(input_file, output_file):
    # Read data from JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize defaultdict to store mean and median
    results = defaultdict(lambda: {'mean': [], 'median': []})
    
    # Calculate mean and median for each key
    for item in data:
        for key, value in item.items():
            results[key]['mean'].append(value)
            results[key]['median'].append(value)
    
    # Calculate the actual mean and median
    for key in results:
        results[key]['mean'] = np.mean(results[key]['mean'])
        results[key]['median'] = np.median(results[key]['median'])
    
    # Write results to CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Field', 'Mean', 'Median'])
        for key, values in results.items():
            writer.writerow([key, values['mean'], values['median']])
    
    return dict(results)