
import matplotlib.pyplot as plt
import numpy as np

def task_func(myList):
    # Convert myList to a numpy array for easier manipulation
    data = np.array(myList)
    
    # Calculate the bin edges to align with integer values in myList
    bin_edges = np.arange(np.min(data) - 0.5, np.max(data) + 1.5, 1)
    
    # Create the histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=bin_edges, edgecolor='black')
    
    # Set the labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Values')
    
    # Return the Axes object
    return ax