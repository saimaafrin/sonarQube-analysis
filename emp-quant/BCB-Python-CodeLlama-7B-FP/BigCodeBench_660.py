import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
def task_func(x, y, labels):
    """
    Scale the "x" and "y" arrays using the standard scaler of sklearn and plot them with given labels. Each pair of x and y arrays are scaled independently and plotted as a separate series with a label.
    The function should output with:
        matplotlib.figure.Figure: The figure object containing the plot.
    """
    # Initialize the figure and axis
    fig, ax = plt.subplots()

    # Initialize the scaler
    scaler = StandardScaler()

    # Scale the x and y arrays
    x_scaled = scaler.fit_transform(x)
    y_scaled = scaler.fit_transform(y)

    # Plot the scaled x and y arrays
    ax.plot(x_scaled, label=labels[0])
    ax.plot(y_scaled, label=labels[1])

    # Set the title and labels
    ax.set_title("Scaled x and y arrays")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Return the figure
    return fig
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
labels = ["x", "y"]