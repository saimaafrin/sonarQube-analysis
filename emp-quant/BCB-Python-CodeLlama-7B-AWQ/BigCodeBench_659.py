import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
def task_func(x, y, labels):
    """
    Draw normal distributions for multiple 'x' and 'y' arrays with labels.
    Each pair (x, y) represents a different chemical compound in the 'labels' list.
    """
    # Check if the input arrays have the same length
    if len(x) != len(y):
        raise ValueError("The input arrays must have the same length")

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Loop through the input arrays and draw the normal distributions
    for i in range(len(x)):
        # Draw the normal distribution for the current compound
        ax.plot(stats.norm.pdf(x[i], y[i], loc=0, scale=1))

        # Set the label for the current compound
        ax.set_xlabel(labels[i])

    # Set the title of the plot
    ax.set_title("Normal Distributions for Chemical Compounds")

    # Return the figure object
    return fig
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
labels = ["Compound 1", "Compound 2", "Compound 3", "Compound 4", "Compound 5"]