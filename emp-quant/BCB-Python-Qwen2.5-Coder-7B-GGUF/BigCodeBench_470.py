
import matplotlib.pyplot as plt
import numpy as np

def task_func(myList):
    # Convert myList to a numpy array for easier manipulation
    data = np.array(myList)
    
    # Determine the bin edges by finding the minimum and maximum values in myList
    # and adjusting them to align with integer values
    min_val = np.floor(np.min(data))
    max_val = np.ceil(np.max(data))
    bins = np.arange(min_val, max_val + 1)
    
    # Create the histogram with the specified bin edges
    ax = plt.hist(data, bins=bins, edgecolor='black')
    
    # Set the labels and title
    ax[0].set_xlabel('Value')
    ax[0].set_ylabel('Frequency')
    ax[0].set_title('Histogram of Values')
    
    # Return the Axes object
    return ax[0]