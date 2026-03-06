
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle

COLORS = ["b", "g", "r", "c", "m", "y", "k"]

def task_func(list_of_lists):
    # Create a figure and axes objects
    fig, ax = plt.subplots()

    # Create a cycle object for the colors
    color_cycle = cycle(COLORS)

    # Iterate over the inner lists of the input list
    for i, inner_list in enumerate(list_of_lists):
        # Shuffle the y-values of the inner list
        shuffled_y_values = np.random.permutation(inner_list)

        # Plot the line with the shuffled y-values and sequential x-values
        ax.plot(range(1, len(inner_list) + 1), shuffled_y_values, color=next(color_cycle))

    # Return the figure and axes objects
    return fig, ax

# Show the plot
plt.show()