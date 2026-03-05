
import pandas as pd
import numpy as np

def task_func(L):
    # Check if input is a list of lists of integers
    if not all(isinstance(sublist, list) and all(isinstance(item, int) for item in sublist) for sublist in L):
        raise TypeError("Input must be a list of lists of integers")

    # Convert nested list to 1D numpy array
    arr = np.array(L)

    # Create histogram of unique values
    unique_vals, counts = np.unique(arr, return_counts=True)

    # Create pandas DataFrame with unique values and counts
    df = pd.DataFrame({"Unique Values": unique_vals, "Counts": counts})

    # Plot histogram with rwidth 0.8
    ax = df.plot.bar(x="Unique Values", y="Counts", rwidth=0.8)

    return ax