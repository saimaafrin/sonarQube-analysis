
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(arr):
    """
    Plots a heatmap of a given 2D numerical array and prints the sum of each row.
    The heatmap's color range is set based on the minimum and maximum values in the array.
    
    Parameters:
    arr (np.ndarray): A 2D numerical array.
    
    Returns:
    ax (matplotlib.axes.Axes): The Axes object with the plotted heatmap.
    """
    # Calculate the sum of each row
    row_sums = np.sum(arr, axis=1)
    print("Row sums:", row_sums)
    
    # Plot the heatmap
    ax = sns.heatmap(arr, cmap='viridis', annot=True, fmt='d', cbar=False)
    plt.show()
    
    return ax