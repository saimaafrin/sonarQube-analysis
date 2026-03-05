import matplotlib.pyplot as plt
import numpy as np
def task_func(n, seed=0):
    """
    Generates a simple scatter plot with 'n' points.
    The function should output with:
        plot (matplotlib.figure.Figure): The generated plot titled "Scatter plot of random points", with x-axis labeled "X" and y-axis labeled "Y".
        points (list of tuples): List containing the (x, y) coordinates of the plotted points.
    """
    np.random.seed(seed)
    x = np.random.rand(n)
    y = np.random.rand(n)
    points = list(zip(x, y))
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Scatter plot of random points")
    return fig, points
n = 10