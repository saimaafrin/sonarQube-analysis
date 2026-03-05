import matplotlib.pyplot as plt
import numpy as np
def task_func(n, seed=0):
    """
    Generates a simple scatter plot with 'n' points.
    The function should output with:
        plot (matplotlib.figure.Figure): The generated plot titled "Scatter plot of random points", with x-axis labeled "X" and y-axis labeled "Y".
        points (list of tuples): List containing the (x, y) coordinates of the plotted points.
    """
    # Set random seed for reproducibility
    np.random.seed(seed)

    # Generate random x and y coordinates
    x = np.random.uniform(0, 10, n)
    y = np.random.uniform(0, 10, n)

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the points
    ax.scatter(x, y, c='blue')

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Set plot title
    ax.set_title('Scatter plot of random points')

    # Return the plot and points
    return fig, (x, y)
n = 100