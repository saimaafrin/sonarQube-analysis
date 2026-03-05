
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_str, separator=",", bins=20):
    # Check if data is empty
    if data_str == "":
        raise ValueError("Data is empty")

    # Convert data to integers
    data = data_str.split(separator)
    data = [int(x) for x in data]

    # Create a pandas Series
    series = pd.Series(data)

    # Plot the histogram
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(series, bins=bins, grid=True, rwidth=0.9, color="#607c8e")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of the data")
    plt.show()

    return series, ax