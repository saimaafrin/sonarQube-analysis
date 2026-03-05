import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(data):
    # Convert the input string to a pandas Series
    data_series = pd.Series(list(map(int, data.split(','))))
    
    # Calculate the bins for the histogram
    bins = np.arange(data_series.min(), data_series.max() + 2) - 0.5
    
    # Create the histogram
    ax = data_series.hist(bins=bins, edgecolor='black')
    
    # Set the labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Values')
    
    # Return the Axes object
    return ax