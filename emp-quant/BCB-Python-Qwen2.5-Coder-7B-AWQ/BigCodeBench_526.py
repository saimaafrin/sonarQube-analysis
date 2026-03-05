import json
import pandas as pd
import numpy as np
from collections import defaultdict
def task_func(input_file="data.json"):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize a defaultdict to store the sums, counts, and medians
    sums = defaultdict(float)
    counts = defaultdict(int)
    medians = defaultdict(list)
    
    # Process each dictionary in the list
    for item in data:
        for key, value in item.items():
            if isinstance(value, (int, float)):
                sums[key] += value
                counts[key] += 1
                medians[key].append(value)
    
    # Calculate mean and median for each key
    means = {key: sums[key] / counts[key] if counts[key] > 0 else np.nan for key in sums}
    medians = {key: np.median(medians[key]) if medians[key] else np.nan for key in medians}
    
    # Create a DataFrame
    df = pd.DataFrame({'mean': means, 'median': medians})
    
    # Sort the DataFrame by index
    df = df.sort_index()
    
    return df