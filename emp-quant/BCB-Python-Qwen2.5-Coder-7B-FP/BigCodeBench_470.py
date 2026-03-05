import matplotlib.pyplot as plt
import numpy as np
def task_func(myList):
    """
    Draws a histogram of the values in a list and returns the plot's Axes.

    Parameters:
    myList (list): A list of numerical values.

    Returns:
    ax (matplotlib.axes._axes.Axes): Axes object of the histogram plot.
    """
    # Convert the list to a numpy array for easier manipulation
    data = np.array(myList)
    
    # Calculate the bin edges to align with integer values in myList
    bin_edges = np.arange(np.floor(data.min()) - 0.5, np.ceil(data.max()) + 1.5, 1)
    
    # Create the histogram plot
    ax = plt.hist(data, bins=bin_edges, edgecolor='black')
    
    # Set the labels and title
    ax[0].set_xlabel('Value')
    ax[0].set_ylabel('Frequency')
    ax[0].set_title('Histogram of Values')
    
    # Return the Axes object
    return ax[0]