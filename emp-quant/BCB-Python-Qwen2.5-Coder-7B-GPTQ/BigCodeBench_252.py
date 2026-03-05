import matplotlib.pyplot as plt
from itertools import zip_longest
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
    # Create a figure and an axes.
    fig, ax = plt.subplots()
    
    # Cycle through the colors and labels using zip_longest
    for series, label, color in zip_longest(data, labels, COLORS, fillvalue='black'):
        ax.plot(series, label=label, color=color)
    
    # Add a legend to the plot
    ax.legend()
    
    # Return the axes object
    return ax
data = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 3, 2, 3, 2],
    [3, 2, 3, 2, 3],
    [4, 3, 4, 3, 4]
]
labels = ['Series 1', 'Series 2', 'Series 3', 'Series 4', 'Series 5']