
import matplotlib.pyplot as plt
import numpy as np

def task_func(n, seed=0):
    """
    Generates a simple scatter plot with 'n' points.

    Parameters:
    n (int): The number of points to generate.
    seed (int): The seed for the random number generator for reproducibility.

    Returns:
    plot (matplotlib.figure.Figure): The generated plot titled "Scatter plot of random points", with x-axis labeled "X" and y-axis labeled "Y".
    points (list of tuples): List containing the (x, y) coordinates of the plotted points.
    """
    # Set the seed for the random number generator
    np.random.seed(seed)
    
    # Generate 'n' random points
    x = np.random.rand(n)
    y = np.random.rand(n)
    points = list(zip(x, y))
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the points
    ax.scatter(x, y)
    
    # Set the title and labels
    ax.set_title("Scatter plot of random points")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    
    return fig, points