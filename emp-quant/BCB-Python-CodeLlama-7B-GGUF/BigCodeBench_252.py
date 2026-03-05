
import matplotlib.pyplot as plt
from itertools import zip_longest

# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']

def task_func(data, labels):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Create a list of colors to use
    colors = COLORS * len(data)
    if len(colors) < len(data):
        colors = colors + ['black'] * (len(data) - len(colors))

    # Create a list of labels to use
    labels = labels * len(data)
    if len(labels) < len(data):
        labels = labels + [''] * (len(data) - len(labels))

    # Plot the data
    for i, (x, y) in enumerate(zip_longest(data, labels)):
        ax.plot(x, y, color=colors[i])

    # Set the title and labels
    ax.set_title('Plot with different colors')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Return the Axes object
    return ax