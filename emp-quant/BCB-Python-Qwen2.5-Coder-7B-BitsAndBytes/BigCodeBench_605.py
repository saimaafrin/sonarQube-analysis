
import pandas as pd
import matplotlib.pyplot as plt

def task_func(matrix):
    """
    Visualize a 2D numeric array (matrix) as a heatmap using matplotlib.

    Parameters:
    matrix (list of lists or numpy.ndarray): A 2D numeric array.

    Returns:
    ax (matplotlib.axes._axes.Axes): The Axes object with the heatmap.
    """
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the heatmap
    cax = ax.matshow(matrix, cmap='hot', interpolation='nearest')

    # Add a colorbar
    fig.colorbar(cax)

    return ax

    # Get the Axes object
    ax = task_func(sample_matrix)

    # Show the plot
    plt.show()