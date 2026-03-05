
import pandas as pd
import matplotlib.pyplot as plt

def task_func(matrix):
    """
    Visualize a 2D numeric array (matrix) as a heatmap using matplotlib.

    Parameters:
    matrix (np.array): A 2D numpy array to be visualized as a heatmap.

    Returns:
    ax (matplotlib.axes._axes.Axes): The Axes object with the heatmap.
    """
    fig, ax = plt.subplots()
    heatmap = ax.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.colorbar(heatmap)
    return ax