
import json
import pandas as pd
import numpy as np
from collections import defaultdict

def task_func(input_file="data.json"):
    # Read the JSON data from the file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Initialize a defaultdict to store the sums and counts for each key
    sums = defaultdict(float)
    counts = defaultdict(int)

    # Iterate over the list of dictionaries
    for item in data:
        for key, value in item.items():
            if isinstance(value, (int, float)):
                sums[key] += value
                counts[key] += 1

    # Calculate the mean and median for each key
    means = {key: sums[key] / counts[key] for key in sums}
    medians = {key: np.median([value for value in sums[key]]) for key in sums}

    # Create a DataFrame with the results
    df = pd.DataFrame({
        'mean': [means[key] for key in means],
        'median': [medians[key] for key in medians]
    }, index=means.keys())

    # Sort the DataFrame by the index (variable names)
    df = df.sort_index()

    return df