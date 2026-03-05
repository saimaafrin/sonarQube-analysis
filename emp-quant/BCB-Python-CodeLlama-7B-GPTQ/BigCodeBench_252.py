import matplotlib.pyplot as plt
from itertools import zip_longest
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']
def task_func(data, labels):
    """
    Plot a list of data with different colors. If there are more data series than the predefined colors, the function cycles through the colors. In case of even more series than colors + labels, 'black' is used.
    The function should output with:
        matplotlib.axes.Axes: The Axes object of the plot.
    """
    # Check if the number of data series is less than the number of predefined colors
    if len(data) <= len(COLORS):
        # Create a list of colors with the same length as the number of data series
        colors = COLORS[:len(data)]
    # Check if the number of data series is more than the number of predefined colors
    else:
        # Create a list of colors with the same length as the number of data series
        colors = COLORS * (len(data) // len(COLORS))
        # Add 'black' to the list of colors if there are more data series than colors + labels
        if len(data) > len(COLORS) + len(labels):
            colors.append('black')

    # Create a list of data series with the same length as the number of data series
    data_series = [data[i] for i in range(len(data))]

    # Create a list of labels with the same length as the number of data series
    labels = [labels[i] for i in range(len(labels))]

    # Create a figure and an axes object
    fig, ax = plt.subplots()

    # Plot the data series with the corresponding colors
    for i in range(len(data_series)):
        ax.plot(data_series[i], color=colors[i])

    # Set the labels for the x-axis and the y-axis
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    # Set the title of the plot
    ax.set_title('Plot of data with different colors')

    # Return the Axes object of the plot
    return ax
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']