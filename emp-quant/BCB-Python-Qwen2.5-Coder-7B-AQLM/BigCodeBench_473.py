
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(n_walks, n_steps, seed=None):
    """
    Generates and plots n_walks number of random walks, each with n_steps steps.
    
    Parameters:
    - n_walks (int): The number of random walks to generate.
    - n_steps (int): The number of steps in each random walk.
    - seed (int, optional): Seed for the random number generator for reproducibility.
    
    Returns:
    - ax (plt.Axes): A Matplotlib Axes containing the plotted random walks.
    """
    # Validate inputs
    if not isinstance(n_walks, int) or n_walks <= 0:
        raise ValueError("n_walks must be a positive integer.")
    if not isinstance(n_steps, int) or n_steps <= 0:
        raise ValueError("n_steps must be a positive integer.")
    
    # Set seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Define colors for the walks
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    color_cycle = itertools.cycle(colors)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Generate and plot each random walk
    for _ in range(n_walks):
        walk = np.cumsum(np.random.randn(n_steps))
        ax.plot(walk, next(color_cycle))
    
    # Set title and labels
    ax.set_title(f"{n_walks} Random Walks")
    ax.set_xlabel("Steps")
    ax.set_ylabel("Position")
    
    # Return the axis
    return ax