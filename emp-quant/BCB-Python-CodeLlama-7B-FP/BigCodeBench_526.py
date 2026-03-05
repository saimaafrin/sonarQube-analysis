import json
import pandas as pd
import numpy as np
from collections import defaultdict
def task_func(input_file="data.json"):
    # Read the JSON file
    with open(input_file, "r") as f:
        data = json.load(f)

    # Create a dictionary to store the mean and median values for each key
    means_and_medians = defaultdict(list)

    # Iterate over the data and calculate the mean and median for each key
    for d in data:
        for key, value in d.items():
            if isinstance(value, (int, float)):
                means_and_medians[key].append(value)

    # Calculate the mean and median for each key
    means = {key: np.mean(values) for key, values in means_and_medians.items()}
    medians = {key: np.median(values) for key, values in means_and_medians.items()}

    # Create a DataFrame with the mean and median values for each key
    df = pd.DataFrame(index=means_and_medians.keys(), columns=["mean", "median"])
    df["mean"] = df.index.map(means)
    df["median"] = df.index.map(medians)

    # Sort the DataFrame by the variable names (keys)
    df.sort_index(inplace=True)

    return df
input_file = "data.json"