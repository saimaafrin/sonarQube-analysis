
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(n_walks, n_steps, seed=None):
    """
    Generates and plots multiple random walks.

    Parameters:
    - n_walks (int): Number of random walks to generate.
    - n_steps (int): Number of steps per random walk.
    - seed (int, optional): Seed for the random number generator for reproducibility.

    Returns:
    - ax (plt.Axes): A Matplotlib Axes containing the plotted random walks.
    """
    if not isinstance(n_walks, int) or n_walks <= 0:
        raise ValueError("n_walks must be a positive integer.")
    if not isinstance(n_steps, int) or n_steps <= 0:
        raise ValueError("n_steps must be a positive integer.")

    # Set up the figure and axis
    fig, ax = plt.subplots()

    # Define the colors for the walks
    colors = list(itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k']))

    # Generate and plot the random walks
    for i in range(n_walks):
        # Generate random steps
        steps = np.random.choice([-1, 1], size=n_steps)
        # Calculate the positions of the walk
        positions = np.cumsum(steps)
        # Plot the walk
        ax.plot(positions, color=colors[i % len(colors)])

    return ax