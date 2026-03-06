
import matplotlib.pyplot as plt
from itertools import zip_longest

# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']

def task_func(data, labels):
    # Create a figure and an axes object
    fig, ax = plt.subplots()

    # Plot the data with different colors
    for i, (data_series, label) in enumerate(zip_longest(data, labels)):
        color = COLORS[i % len(COLORS)]
        ax.plot(data_series, label=label, color=color)

    # Add a legend
    ax.legend()

    # Return the axes object
    return ax