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
        raise ValueError("The length of the 'x' and 'y' arrays must be the same.")

    # Check if the input labels are valid
    if not isinstance(labels, list):
        raise ValueError("The 'labels' argument must be a list.")
    if len(labels) != len(x):
        raise ValueError("The length of the 'labels' list must be the same as the length of the 'x' and 'y' arrays.")

    # Create a figure object
    fig, ax = plt.subplots()

    # Draw normal distributions for each pair of 'x' and 'y' arrays
    for i in range(len(x)):
        ax.plot(x[i], y[i], label=labels[i])

    # Set the title and labels
    ax.set_title("Normal Distributions for Chemical Compounds")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Return the figure object
    return fig
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
labels = ["Compound 1", "Compound 2", "Compound 3", "Compound 4", "Compound 5"]