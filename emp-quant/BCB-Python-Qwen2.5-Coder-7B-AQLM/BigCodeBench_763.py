
import numpy as np
from collections import defaultdict
import json
import csv

# Constants
def task_func(input_file, output_file):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize a dictionary to store the means and medians
    results = defaultdict(lambda: {'mean': [], 'median': []})
    
    # Iterate over each dictionary in the list
    for item in data:
        for key, value in item.items():
            results[key]['mean'].append(value)
            results[key]['median'].append(value)
    
    # Calculate the mean and median for each key
    for key in results:
        results[key]['mean'] = np.mean(results[key]['mean'])
        results[key]['median'] = np.median(results[key]['median'])
    
    # Write the results to a CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Key', 'Mean', 'Median'])
        for key, values in results.items():
            writer.writerow([key, values['mean'], values['median']])
    
    # Return the results dictionary
    return dict(results)