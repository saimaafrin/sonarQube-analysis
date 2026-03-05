import matplotlib.pyplot as plt
import random
COLORS = ['#00bfbf', '#000000', '#0000ff']
def task_func(number_list, bins):
    """
    Create a histogram subplot of a list of numbers.

    Args:
        number_list (list): List of numbers to be plotted.
        bins (int): Number of bins to use for the histogram.

    Returns:
        matplotlib.axes._axes.Axes: The axes object representing the histogram plot.
    """
    # Create a figure and an axes object
    fig, ax = plt.subplots()

    # Set the title, x-axis label, and y-axis label
    ax.set_title('Histogram')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')

    # Set the color of the histogram bars randomly
    color = random.choice(COLORS)

    # Plot the histogram
    ax.hist(number_list, bins=bins, color=color)

    # Return the axes object
    return ax
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bins = 5