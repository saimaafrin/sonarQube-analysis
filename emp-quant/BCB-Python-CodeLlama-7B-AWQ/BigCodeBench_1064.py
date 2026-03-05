import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(arr):
    """
    Plots a heatmap of a given 2D numerical array and prints the sum of each row.
    The heatmap's color range is set based on the minimum and maximum values in the array.
    """
    # Calculate the sum of each row
    row_sums = arr.sum(axis=1)

    # Set the color range based on the minimum and maximum values in the array
    vmin = arr.min()
    vmax = arr.max()

    # Plot the heatmap
    ax = sns.heatmap(arr, cmap="coolwarm", vmin=vmin, vmax=vmax)

    # Print the sum of each row
    print(row_sums)

    return ax
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])