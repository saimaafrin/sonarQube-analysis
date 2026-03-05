import matplotlib.pyplot as plt
import random
COLORS = ['#00bfbf', '#000000', '#0000ff']
def task_func(number_list, bins):
    """
    Create a histogram subplot of a list of numbers.

    Args:
        number_list (list): List of numbers to be plotted.
        bins (int): Number of bins for the histogram.

    Returns:
        matplotlib.axes._axes.Axes: The axes object representing the histogram plot.
    """
    # Generate a random color for the histogram bars
    color = random.choice(COLORS)

    # Create the histogram plot
    fig, ax = plt.subplots()
    ax.hist(number_list, bins=bins, color=color)

    # Set the plot title, x-axis label, and y-axis label
    ax.set_title('Histogram')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')

    # Return the axes object
    return ax
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bins = 5