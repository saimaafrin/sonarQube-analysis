
import matplotlib.pyplot as plt
import numpy as np

def task_func(myList):
    # Convert myList to a numpy array for easier manipulation
    data = np.array(myList)
    
    # Calculate the bin edges to align with integer values
    bin_edges = np.arange(np.floor(data.min()), np.ceil(data.max()) + 1)
    
    # Create the histogram
    ax = plt.hist(data, bins=bin_edges, edgecolor='black')
    
    # Set the labels and title
    ax[0].set_xlabel('Value')
    ax[0].set_ylabel('Frequency')
    ax[0].set_title('Histogram of Values')
    
    # Return the Axes object
    return ax[0]