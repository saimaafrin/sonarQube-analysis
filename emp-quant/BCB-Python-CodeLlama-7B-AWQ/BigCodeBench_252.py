import matplotlib.pyplot as plt
from itertools import zip_longest
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']
def task_func(data, labels):
    """
    Plot a list of data with different colors. If there are more data series than the predefined colors, the function cycles through the colors. In case of even more series than colors + labels, 'black' is used.
    The function should output with:
        matplotlib.axes.Axes: The Axes object of the plot.
    """
    # Check if the number of data series is greater than the number of colors
    if len(data) > len(COLORS):
        # Cycle through the colors
        colors = itertools.cycle(COLORS)
    else:
        # Use the predefined colors
        colors = COLORS
    # Create a figure and axis
    fig, ax = plt.subplots()
    # Plot the data
    for i, (data_series, label) in enumerate(zip_longest(data, labels)):
        # Check if the label is None
        if label is None:
            # Use the default label
            label = 'Series {}'.format(i)
        # Plot the data series
        ax.plot(data_series, label=label, color=next(colors))
    # Set the title and labels
    ax.set_title('Data Plot')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    # Return the Axes object
    return ax