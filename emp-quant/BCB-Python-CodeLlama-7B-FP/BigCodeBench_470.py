import matplotlib.pyplot as plt
import numpy as np
def task_func(myList):
    """
    Draws a histogram of the values in a list and returns the plot's Axes.
    For visualization:
    - Bin edges are adjusted to align with integer values in `myList`.
    - Histogram bars are outlined in black.
    - X-axis label: 'Value'
    - Y-axis label: 'Frequency'
    - Plot title: 'Histogram of Values'
    """
    # Create a histogram plot
    ax = plt.hist(myList, bins=np.arange(min(myList), max(myList) + 1, 1), edgecolor='black')

    # Adjust the bin edges to align with integer values in `myList`
    ax.set_xlim(min(myList), max(myList))

    # Set the x-axis label
    ax.set_xlabel('Value')

    # Set the y-axis label
    ax.set_ylabel('Frequency')

    # Set the plot title
    ax.set_title('Histogram of Values')

    return ax
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]