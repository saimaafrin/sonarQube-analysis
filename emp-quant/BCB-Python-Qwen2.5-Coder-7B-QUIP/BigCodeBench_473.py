
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(n_walks, n_steps, seed=None):
    """
    Generates and plots a specified number of random walks.

    Parameters:
    n_walks (int): The number of random walks to generate.
    n_steps (int): The number of steps in each walk.
    seed (int, optional): The seed for the random number generator. Defaults to None.

    Returns:
    ax (plt.Axes): A Matplotlib Axes containing the plotted random walks.
    """
    # Validate input parameters
    if not isinstance(n_walks, int) or n_walks <= 0:
        raise ValueError("n_walks must be a positive integer")
    if not isinstance(n_steps, int) or n_steps <= 0:
        raise ValueError("n_steps must be a positive integer")
    
    # Set random seed if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random walks
    walks = np.random.randn(n_walks, n_steps)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot each walk with a different color
    colors = itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
    for walk in walks:
        ax.plot(walk, color=next(colors))
    
    # Return the axes object
    return ax