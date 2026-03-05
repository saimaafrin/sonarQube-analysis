import numpy as np
from collections import defaultdict
import json
import csv
def task_func(input_file, output_file):
    # Read data from JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize a dictionary to store mean and median
    results = defaultdict(dict)
    
    # Iterate over each dictionary in the list
    for item in data:
        for key, value in item.items():
            if isinstance(value, (int, float)):
                # Calculate mean and median
                mean_value = np.mean([item[key] for item in data])
                median_value = np.median([item[key] for item in data])
                # Store the results
                results[key]['mean'] = mean_value
                results[key]['median'] = median_value
    
    # Write results to CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Field', 'Mean', 'Median'])
        for key, values in results.items():
            writer.writerow([key, values['mean'], values['median']])
    
    return results