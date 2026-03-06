
import matplotlib.pyplot as plt
import random

# Constants
COLORS = ['#00bfbf', '#000000', '#0000ff']

def task_func(number_list, bins):
    """
    Generates a histogram plot for the given list of numbers.

    Parameters:
    number_list (list): A list of numbers to be plotted.
    bins (int): The number of bins to use in the histogram.

    Returns:
    matplotlib.axes._axes.Axes: The axes object representing the histogram plot.
    """
    # Select a random color from the predefined set of colors
    color = random.choice(COLORS)

    # Create a figure and an axes object
    fig, ax = plt.subplots()

    # Plot the histogram
    n, bins, patches = ax.hist(number_list, bins=bins, color=color)

    # Set the plot title and axis labels
    ax.set_title('Histogram')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')

    # Return the axes object
    return ax