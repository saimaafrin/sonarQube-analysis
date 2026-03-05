import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_str, separator=",", bins=20):
    """
    Convert a string of numerical values separated by a specified separator into a pandas numerical series with int64, and then draw a histogram of the data.
    The function raises a ValueError if data is empty or it fails to convert the data.
    It plots the histogram with the following attributes:
        - grid: True
        - rwidth: 0.9
        - color: '#607c8e'
    The function should output with:
        tuple: A tuple containing:
        1. Series: A pandas Series of the data converted into integers.
        2. Axes: The Axes object of the plotted histogram.
    """
    # Check if data is empty
    if not data_str:
        raise ValueError("Data is empty")

    # Convert data to integers
    try:
        data = pd.Series(data_str.split(separator))
        data = data.astype(np.int64)
    except ValueError:
        raise ValueError("Failed to convert data")

    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, grid=True, rwidth=0.9, color='#607c8e')
    ax.set_title("Histogram of Data")
    ax.set_xlabel("Data")
    ax.set_ylabel("Frequency")
    plt.show()

    # Return tuple of series and axes
    return data, ax
data_str = "1,2,3,4,5,6,7,8,9,10"
separator = ","
bins = 20