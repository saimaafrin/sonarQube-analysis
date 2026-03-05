import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(n_walks, n_steps, seed=None):
    """
    Generate and plot n_walks number of random walks, each with n_steps steps.
    
    Parameters:
    - n_walks (int): Number of random walks to generate.
    - n_steps (int): Number of steps in each random walk.
    - seed (int, optional): Seed for the random number generator for reproducibility.
    
    Returns:
    - ax (plt.Axes): A Matplotlib Axes containing the plotted random walks.
    """
    # Check for valid n_walks and n_steps
    if not isinstance(n_walks, int) or n_walks <= 0:
        raise ValueError("n_walks must be a positive integer")
    if not isinstance(n_steps, int) or n_steps <= 0:
        raise ValueError("n_steps must be a positive integer")
    
    # Set the seed for reproducibility if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Define the colors for the walks
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    color_cycle = itertools.cycle(colors)
    
    # Create a figure and an axes
    fig, ax = plt.subplots()
    
    # Generate and plot each random walk
    for _ in range(n_walks):
        # Generate random steps
        steps = np.random.choice([-1, 1], size=n_steps)
        # Compute the cumulative sum to get the walk positions
        walk = np.cumsum(steps)
        # Plot the walk with a color from the cycle
        ax.plot(walk, color=next(color_cycle))
    
    # Set the title and labels
    ax.set_title(f"{n_walks} Random Walks")
    ax.set_xlabel("Steps")
    ax.set_ylabel("Position")
    
    # Return the axes
    return ax