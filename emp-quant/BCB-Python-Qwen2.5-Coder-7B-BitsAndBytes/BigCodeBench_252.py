
import matplotlib.pyplot as plt
from itertools import cycle

# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']

def task_func(data, labels):
    """
    Plot a list of data with different colors. If there are more data series than the predefined colors,
    the function cycles through the colors. In case of even more series than colors + labels, 'black' is used.

    Parameters:
    data (list of lists): A list where each element is a list of data points for one series.
    labels (list of str): A list of labels for each data series.

    Returns:
    matplotlib.axes.Axes: The Axes object of the plot.
    """
    # Create a figure and an axes.
    fig, ax = plt.subplots()

    # Cycle through the colors using itertools.cycle
    color_cycle = cycle(COLORS)

    # Plot each data series
    for i, (series_data, label) in enumerate(zip(data, labels)):
        color = next(color_cycle)
        if i >= len(labels):
            color = 'black'
        ax.plot(series_data, label=label, color=color)

    # Add legend to the plot
    ax.legend()

    return ax

ax = task_func(data, labels)
plt.show()