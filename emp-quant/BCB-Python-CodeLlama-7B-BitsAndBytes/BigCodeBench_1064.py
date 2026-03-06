
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(arr):
    # Calculate the sum of each row
    row_sums = arr.sum(axis=1)

    # Set the color range based on the minimum and maximum values in the array
    vmin = arr.min()
    vmax = arr.max()

    # Plot the heatmap
    ax = sns.heatmap(arr, cmap="YlGnBu", vmin=vmin, vmax=vmax)

    # Print the sum of each row
    print("Row sums:")
    print(row_sums)

    return ax