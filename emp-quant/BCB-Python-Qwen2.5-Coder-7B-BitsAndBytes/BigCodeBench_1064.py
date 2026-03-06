
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(arr):
    """
    Plots a heatmap of a given 2D numerical array and prints the sum of each row.
    
    Parameters:
    arr (np.ndarray): A 2D numpy array to plot as a heatmap.
    
    Returns:
    ax (matplotlib.axes.Axes): The Axes object with the plotted heatmap.
    """
    # Calculate the sum of each row
    row_sums = np.sum(arr, axis=1)
    print("Sum of each row:", row_sums)
    
    # Plotting the heatmap
    min_val = arr.min()
    max_val = arr.max()
    ax = sns.heatmap(arr, cmap='viridis', vmin=min_val, vmax=max_val, annot=False, fmt="d")
    
    # Display the plot
    plt.show()
    
    return ax