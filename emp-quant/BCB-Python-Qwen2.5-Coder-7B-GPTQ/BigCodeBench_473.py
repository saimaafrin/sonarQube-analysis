import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(n_walks, n_steps, seed=None):
    """
    Generate and plot n_walks number of random walks, each with n_steps steps.
    
    Parameters:
    - n_walks (int): Number of random walks to generate.
    - n_steps (int): Number of steps in each walk.
    - seed (int, optional): Seed for the random number generator for reproducibility.
    
    Returns:
    - ax (plt.Axes): A Matplotlib Axes containing the plotted random walks.
    """
    # Validate inputs
    if not isinstance(n_walks, int) or n_walks <= 0:
        raise ValueError("n_walks must be a positive integer.")
    if not isinstance(n_steps, int) or n_steps <= 0:
        raise ValueError("n_steps must be a positive integer.")
    
    # Set seed for reproducibility if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Define colors for the walks
    colors = list(itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k']))
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Generate and plot each walk
    for _ in range(n_walks):
        # Generate random steps
        steps = np.random.choice([-1, 1], size=n_steps)
        # Calculate positions
        positions = np.cumsum(steps)
        # Plot the walk
        ax.plot(positions, color=next(colors))
    
    # Set labels and title
    ax.set_xlabel('Steps')
    ax.set_ylabel('Position')
    ax.set_title('Random Walks')
    
    # Return the axis
    return ax