
import matplotlib.pyplot as plt
from itertools import zip_longest
# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']

def task_func(data, labels):
    """
    Plot a list of data with different colors. If there are more data series than the predefined colors,
    the function cycles through the colors. In case of even more series than colors + labels, 'black' is used.
    
    Parameters:
    data (list of lists): A list of data series to plot.
    labels (list of str): A list of labels for each data series.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plot.
    """
    fig, ax = plt.subplots()
    for series, label, color in zip_longest(data, labels, COLORS, fillvalue='black'):
        ax.plot(series, label=label, color=color)
    ax.legend()
    return ax