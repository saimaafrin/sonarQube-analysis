import pandas as pd
import matplotlib.pyplot as plt
def task_func(matrix):
    """
    Visualize a 2D numeric array (matrix) as a heatmap using matplotlib.

    Parameters:
    matrix (pd.DataFrame): A 2D numeric array to be visualized as a heatmap.

    Returns:
    ax (matplotlib.axes._axes.Axes): The Axes object with the heatmap.
    """
    # Create a figure and an axes.
    fig, ax = plt.subplots()

    # Plot the heatmap using the 'hot' colormap and bicubic interpolation.
    heatmap = ax.imshow(matrix, cmap='hot', interpolation='bicubic')

    # Add a colorbar to the heatmap.
    plt.colorbar(heatmap)

    # Return the axes object with the heatmap.
    return ax