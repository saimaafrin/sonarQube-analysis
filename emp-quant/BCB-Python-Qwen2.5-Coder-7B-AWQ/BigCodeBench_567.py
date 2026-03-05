import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(data):
    """
    Draws a histogram to visualize the frequency distribution of numeric values provided in a string format.
    
    Parameters:
    data (str): A string containing numeric values separated by spaces.
    
    Returns:
    ax (matplotlib.axes._axes.Axes): The Axes object of the created histogram.
    """
    # Convert the string of data into a pandas Series
    data_series = pd.Series(list(map(float, data.split())))
    
    # Calculate the bins for the histogram
    bins = np.arange(data_series.min(), data_series.max() + 2) - 0.5
    
    # Create the histogram
    ax = data_series.plot(kind='hist', bins=bins, edgecolor='black')
    
    # Set the title and labels
    ax.set_title('Histogram of Values')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object
    return ax