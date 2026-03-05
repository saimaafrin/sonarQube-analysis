import json
import pandas as pd
import numpy as np
from collections import defaultdict
def task_func(input_file="data.json"):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize a defaultdict to store the sums and counts for each key
    sums = defaultdict(float)
    counts = defaultdict(int)
    
    # Iterate over each dictionary in the list
    for item in data:
        for key, value in item.items():
            # Check if the value is numeric
            if isinstance(value, (int, float)):
                sums[key] += value
                counts[key] += 1
    
    # Calculate mean and median for each key
    means = {key: sums[key] / counts[key] if counts[key] > 0 else np.nan for key in sums}
    medians = {key: np.median([item[key] for item in data if isinstance(item[key], (int, float))]) if any(isinstance(item[key], (int, float)) for item in data) else np.nan for key in sums}
    
    # Create a DataFrame from the results
    df = pd.DataFrame({'mean': means, 'median': medians})
    
    # Sort the DataFrame by the index (variable names)
    df = df.sort_index()
    
    return df