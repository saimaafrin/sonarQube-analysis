
import pandas as pd
import matplotlib.pyplot as plt

def task_func(matrix):
    # Create a figure with a 1x1 grid
    fig, ax = plt.subplots(1, 1)

    # Set the colormap and interpolation method
    cmap = 'hot'
    interpolation = 'bicubic'

    # Plot the heatmap
    ax.imshow(matrix, cmap=cmap, interpolation=interpolation)

    # Set the figure title and labels
    ax.set_title('Heatmap')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Return the Axes object
    return ax