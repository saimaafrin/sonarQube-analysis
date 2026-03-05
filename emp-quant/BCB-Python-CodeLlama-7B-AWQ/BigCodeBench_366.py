import matplotlib.pyplot as plt
import random
COLORS = ['#00bfbf', '#000000', '#0000ff']
def task_func(number_list, bins):
    """
    Create a histogram subplot of a list of numbers.

    Args:
        number_list (list): List of numbers to create histogram from.
        bins (int): Number of bins to use for histogram.

    Returns:
        matplotlib.axes._axes.Axes: The axes object representing the histogram plot.
    """
    # Create histogram plot
    fig, ax = plt.subplots()
    ax.hist(number_list, bins=bins, color=random.choice(COLORS))

    # Set plot title, x-axis label, and y-axis label
    ax.set_title('Histogram')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')

    return ax