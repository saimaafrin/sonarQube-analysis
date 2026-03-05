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
    # Create a figure and axes object
    fig, ax = plt.subplots()

    # Create a list of colors to use for each inner list
    colors = cycle(COLORS)

    # Iterate over each inner list
    for i, inner_list in enumerate(list_of_lists):
        # Skip empty inner lists
        if not inner_list:
            continue

        # Shuffle the y-values of the inner list
        shuffle(inner_list)

        # Plot the line with the shuffled y-values and sequential x-values
        ax.plot(range(1, len(inner_list) + 1), inner_list, next(colors))

    # Set the title and labels
    ax.set_title("Shuffled Lines")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Return the figure and axes objects
    return fig, ax