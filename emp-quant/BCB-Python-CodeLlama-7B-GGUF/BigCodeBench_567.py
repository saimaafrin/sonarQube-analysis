
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Convert string to numeric values
    data = pd.to_numeric(data)

    # Calculate histogram bins
    bins = np.arange(data.min(), data.max()+2) - 0.5

    # Create histogram
    ax = plt.hist(data, bins=bins, label='Histogram of Values')

    # Set x-axis label
    ax.set_xlabel('Value')

    # Set y-axis label
    ax.set_ylabel('Frequency')

    # Set title
    ax.set_title('Histogram of Values')

    # Return Axes object
    return ax