
import matplotlib.pyplot as plt
import numpy as np

def task_func(myList):
    # Create a histogram of the values in the list
    ax = plt.hist(myList, bins=np.arange(min(myList), max(myList) + 1, 1), edgecolor='black')

    # Adjust the bin edges to align with integer values
    ax.set_xlim(min(myList), max(myList))

    # Set the x-axis label and y-axis label
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    # Set the plot title
    ax.set_title('Histogram of Values')

    return ax