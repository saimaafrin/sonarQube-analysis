
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_str, separator=",", bins=20):
    # Check if data is empty
    if not data_str:
        raise ValueError("Data is empty")

    # Convert data string to a list of integers
    data_list = data_str.split(separator)
    data_list = [int(x) for x in data_list]

    # Create a pandas Series from the list
    data_series = pd.Series(data_list)

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(data_series, bins=bins, grid=True, rwidth=0.9, color='#607c8e')

    # Set the title and labels
    ax.set_title("Histogram of Data")
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")

    # Return the series and axes
    return data_series, ax

# Call the function
series, ax = task_func(data_str, separator, bins)

# Print the series and axes
print(series)
print(ax)