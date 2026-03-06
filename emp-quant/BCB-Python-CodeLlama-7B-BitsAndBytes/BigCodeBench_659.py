
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def task_func(x, y, labels):
    # Create a figure object
    fig, ax = plt.subplots()

    # Plot the normal distributions for each pair of (x, y)
    for i in range(len(x)):
        ax.plot(x[i], y[i], label=labels[i])

    # Add a legend to the plot
    ax.legend()

    # Return the figure object
    return fig