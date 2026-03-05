
import matplotlib.pyplot as plt
from itertools import zip_longest
# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']

def task_func(data, labels):
    """
    Plot a list of data with different colors. If there are more data series than the predefined colors,
    the function cycles through the colors. In case of even more series than colors + labels, 'black' is used.
    
    :param data: A list of lists, where each sublist represents a data series to plot.
    :param labels: A list of strings representing the labels for each data series.
    :return: matplotlib.axes.Axes: The Axes object of the plot.
    """
    fig, ax = plt.subplots()
    for i, (series, label) in enumerate(zip_longest(data, labels, fillvalue='black')):
        ax.plot(series, color=COLORS[i % len(COLORS)], label=label)
    ax.legend()
    return ax