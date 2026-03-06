
import matplotlib.pyplot as plt
import numpy as np

def task_func(myList):
    # Adjust bin edges to align with integer values in myList
    bins = np.arange(min(myList), max(myList) + 2) - 0.5
    
    # Create the histogram
    ax = plt.hist(myList, bins=bins, edgecolor='black')
    
    # Set labels and title
    ax[0].set_xlabel('Value')
    ax[0].set_ylabel('Frequency')
    ax[0].set_title('Histogram of Values')
    
    return ax[0]