import json
import pandas as pd
import numpy as np
from collections import defaultdict
def task_func(input_file="data.json"):
    # Read the JSON file
    with open(input_file, "r") as f:
        data = json.load(f)

    # Create a dictionary to store the results
    results = defaultdict(dict)

    # Iterate over the data and calculate the mean and median for each key
    for d in data:
        for k, v in d.items():
            if isinstance(v, (int, float)):
                results[k]["mean"] = np.mean(v)
                results[k]["median"] = np.median(v)

    # Convert the results to a Pandas DataFrame
    df = pd.DataFrame.from_dict(results, orient="index")

    # Sort the DataFrame by the variable names (keys)
    df = df.sort_index()

    # Add the column names
    df.columns = ["mean", "median"]

    return df
input_file = "data.json"