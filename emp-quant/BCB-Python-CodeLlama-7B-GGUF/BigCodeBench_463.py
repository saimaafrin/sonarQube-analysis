
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_str, separator=",", bins=20):
    # Check if data is empty
    if not data_str:
        raise ValueError("Data is empty")

    # Convert data to numerical series
    data = pd.Series(data_str.split(separator))
    data = data.astype(np.int64)

    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, grid=True, rwidth=0.9, color='#607c8e')
    ax.set_title("Histogram of Data")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    return data, ax