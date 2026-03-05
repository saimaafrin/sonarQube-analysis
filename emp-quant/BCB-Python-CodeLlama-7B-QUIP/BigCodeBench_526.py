
import json
import pandas as pd
import numpy as np
from collections import defaultdict

def task_func(input_file="data.json"):
    # Load the JSON file
    with open(input_file, "r") as f:
        data = json.load(f)

    # Create a dictionary to store the mean and median values for each key
    means = defaultdict(float)
    medians = defaultdict(float)

    # Loop through the data and calculate the mean and median for each key
    for key, value in data.items():
        if isinstance(value, list):
            means[key] = np.mean(value)
            medians[key] = np.median(value)

    # Create a DataFrame with the mean and median values
    df = pd.DataFrame(
        index=list(means.keys()),
        columns=["mean", "median"],
        data=list(zip(means.values(), medians.values()))
    )

    return df