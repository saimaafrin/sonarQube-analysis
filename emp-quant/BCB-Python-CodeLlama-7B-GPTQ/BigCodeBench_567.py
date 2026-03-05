import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(data):
    # Convert the string to a list of numeric values
    data = [float(x) for x in data.split(',')]

    # Calculate the histogram bins
    bins = np.arange(data.min(), data.max() + 2) - 0.5

    # Create the histogram
    ax = plt.hist(data, bins=bins, label='Histogram of Values')

    # Set the x-axis label
    ax.set_xlabel('Value')

    # Set the y-axis label
    ax.set_ylabel('Frequency')

    # Set the title
    ax.set_title('Histogram of Values')

    # Return the Axes object
    return ax
data = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10'