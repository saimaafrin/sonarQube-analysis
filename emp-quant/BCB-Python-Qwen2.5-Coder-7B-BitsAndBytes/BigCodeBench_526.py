
import json
import pandas as pd
import numpy as np
from collections import defaultdict

def task_func(input_file="data.json"):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize defaultdicts to store means and medians
    means = defaultdict(list)
    medians = defaultdict(list)
    
    # Iterate over each dictionary in the list
    for item in data:
        for key, value in item.items():
            if isinstance(value, (int, float)):
                means[key].append(value)
                medians[key].append(value)
    
    # Calculate mean and median for each key
    mean_values = {key: np.mean(values) for key, values in means.items()}
    median_values = {key: np.median(values) for key, values in medians.items()}
    
    # Create a DataFrame from the results
    result_df = pd.DataFrame({
        'mean': mean_values,
        'median': median_values
    })
    
    # Sort the DataFrame by index
    result_df.sort_index(inplace=True)
    
    return result_df