import matplotlib.pyplot as plt
import numpy as np
def task_func(myList):
    """
    Draws a histogram of the values in a list and returns the plot's Axes.

    Parameters:
    myList (list): A list of numerical values to plot in the histogram.

    Returns:
    ax (matplotlib.axes._axes.Axes): Axes object of the histogram plot.
    """
    # Convert the list to a numpy array for easier manipulation
    data = np.array(myList)
    
    # Determine the bin edges by finding the minimum and maximum values in the list
    # and adjusting them to align with integer values
    min_val = np.floor(data.min())
    max_val = np.ceil(data.max())
    bins = np.arange(min_val, max_val + 1.5) - 0.5
    
    # Create the histogram plot
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, edgecolor='black')
    
    # Set the labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Values')
    
    return ax