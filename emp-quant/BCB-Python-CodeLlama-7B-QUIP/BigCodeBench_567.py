
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Calculate the histogram bins
    bins = np.arange(data.min(), data.max()+2) - 0.5

    # Create the histogram
    ax = plt.hist(data, bins=bins, label='Histogram of Values')

    # Set the x-axis label
    ax.set_xlabel('Value')

    # Set the y-axis label
    ax.set_ylabel('Frequency')

    # Set the title
    ax.set_title('Histogram of Values')

    return ax