import matplotlib.pyplot as plt
from itertools import zip_longest
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']
def task_func(data, labels):
    """
    Plot a list of data with different colors. If there are more data series than the predefined colors, the function cycles through the colors. In case of even more series than colors + labels, 'black' is used.
    """
    # Create a figure and an axes object
    fig, ax = plt.subplots()

    # Create a list of colors to use for the data series
    colors = COLORS * len(data)
    if len(colors) < len(data):
        colors = colors + ['black'] * (len(data) - len(colors))

    # Create a list of labels to use for the data series
    labels = labels * len(data)
    if len(labels) < len(data):
        labels = labels + [''] * (len(data) - len(labels))

    # Plot the data series
    for i, (x, y) in enumerate(zip_longest(data, labels)):
        ax.plot(x, y, color=colors[i], label=labels[i])

    # Set the title and labels
    ax.set_title('Data Plot')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Return the Axes object
    return ax
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
labels = ['Data 1', 'Data 2', 'Data 3']