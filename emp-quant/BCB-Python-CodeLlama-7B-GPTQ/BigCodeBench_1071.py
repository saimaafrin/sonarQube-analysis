import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle
COLORS = ["b", "g", "r", "c", "m", "y", "k"]
def task_func(list_of_lists):
    """
    Plots a series of lines for each list in list_of_lists. Each line is plotted with shuffled y-values and sequential x-values starting from 1. The function shuffles the y-values of each inner list before plotting. Each line is plotted with a different color from a predetermined set of colors. The function cycles through these colors for each inner list.
    Note that:
        - If an inner list is empty, it will be skipped and no line will be plotted for it.
        - The colors are reused cyclically if there are more inner lists than colors available.
        - The shuffling of y-values is random and different each time the function is called, unless a random seed is set externally.
        - The function uses a default set of colors defined in the COLORS constant.
    The function should output with:
        tuple: A tuple containing the figure and axes objects of the plotted graph.
    """
    # Create a figure and axes objects
    fig, ax = plt.subplots()

    # Create a cycle object for the colors
    color_cycle = cycle(COLORS)

    # Iterate over the inner lists in list_of_lists
    for i, inner_list in enumerate(list_of_lists):
        # Skip empty inner lists
        if not inner_list:
            continue

        # Shuffle the y-values of the inner list
        shuffled_y_values = np.random.permutation(inner_list)

        # Plot the line with the shuffled y-values and sequential x-values
        ax.plot(range(1, len(shuffled_y_values) + 1), shuffled_y_values, color=next(color_cycle))

    # Set the title and labels
    ax.set_title("Shuffled Lines")
    ax.set_xlabel("X-values")
    ax.set_ylabel("Y-values")

    # Return the figure and axes objects
    return fig, ax
list_of_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27],
    [28, 29, 30],
]