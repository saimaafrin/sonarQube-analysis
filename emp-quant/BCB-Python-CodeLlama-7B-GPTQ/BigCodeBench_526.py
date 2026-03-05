import json
import pandas as pd
import numpy as np
from collections import defaultdict
def task_func(input_file="data.json"):
    # Read the JSON file
    with open(input_file, "r") as f:
        data = json.load(f)

    # Create a dictionary to store the mean and median values for each key
    means = defaultdict(list)
    medians = defaultdict(list)

    # Iterate over the data and calculate the mean and median for each key
    for row in data:
        for key, value in row.items():
            if isinstance(value, (int, float)):
                means[key].append(value)
                medians[key].append(value)

    # Calculate the mean and median for each key
    for key in means:
        means[key] = np.mean(means[key])
        medians[key] = np.median(medians[key])

    # Create a Pandas DataFrame with the mean and median values
    df = pd.DataFrame(means, index=sorted(means.keys()))
    df["median"] = medians

    return df
input_file = "data.json"