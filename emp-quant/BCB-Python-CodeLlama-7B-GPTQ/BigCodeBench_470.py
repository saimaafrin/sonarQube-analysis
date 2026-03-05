import matplotlib.pyplot as plt
import numpy as np
def task_func(myList):
    # Create a histogram of the values in the list
    ax = plt.hist(myList, bins=np.arange(min(myList), max(myList) + 1, 1))

    # Adjust the bin edges to align with integer values in the list
    ax.set_xlim(min(myList), max(myList))
    ax.set_xticks(np.arange(min(myList), max(myList) + 1, 1))

    # Outline the histogram bars in black
    for bar in ax.patches:
        bar.set_edgecolor('black')

    # Set the x-axis label and y-axis label
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    # Set the plot title
    ax.set_title('Histogram of Values')

    return ax
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]