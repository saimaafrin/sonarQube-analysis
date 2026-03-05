
import matplotlib.pyplot as plt
import numpy as np

def task_func(myList):
    # Adjust bin edges to align with integer values
    bin_edges = np.arange(min(myList), max(myList) + 1)
    # Create histogram plot
    ax = plt.hist(myList, bins=bin_edges, color='black', alpha=1.0)
    # Set x-axis label and y-axis label
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    # Set plot title
    ax.set_title('Histogram of Values')
    return ax