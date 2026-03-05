
import numpy as np
import seaborn as sns
def task_func(arr):
    # Calculate the sum of each row
    row_sums = np.sum(arr, axis=1)
    # Set the color range based on the minimum and maximum values in the array
    vmin = np.min(arr)
    vmax = np.max(arr)
    # Plot the heatmap
    ax = sns.heatmap(arr, cmap='viridis', vmin=vmin, vmax=vmax)
    # Print the sum of each row
    for i in range(arr.shape[0]):
        print(f"Row {i}: {row_sums[i]}")
    return ax