import matplotlib.pyplot as plt
import numpy as np
def task_func(n, seed=0):
    """
    Generates a simple scatter plot with 'n' points.

    Parameters:
    n (int): The number of points to generate.
    seed (int, optional): The seed for the random number generator. Defaults to 0.

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
    
    # Create a new figure
    fig = plt.figure()
    
    # Create a scatter plot
    plt.scatter(x, y)
    
    # Set the title and labels
    plt.title("Scatter plot of random points")
    plt.xlabel("X")
    plt.ylabel("Y")
    
    return fig, points