import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(n_walks, n_steps, seed=None):
    """
    Create and plot n_walks number of random walks, each with n_steps steps.
    The function checks for valid n_walks and n_steps, then generates walks via numpy.
    Each walk is plotted in a different color cycling through a predefined set of colors: ['b', 'g', 'r', 'c', 'm', 'y', 'k'].
    The function should output with:
        ax (plt.Axes): A Matplotlib Axes containing the plotted random walks.
    """
    # Check for valid n_walks and n_steps
    if n_walks < 1 or n_steps < 1:
        raise ValueError("n_walks and n_steps must be positive integers")

    # Generate random walks
    walks = np.random.randint(0, n_steps, size=(n_walks, n_steps))

    # Create a list of colors
    colors = itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k'])

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the walks
    for i, walk in enumerate(walks):
        ax.plot(walk, color=next(colors))

    # Set the title and labels
    ax.set_title("Random Walks")
    ax.set_xlabel("Step")
    ax.set_ylabel("Position")

    # Return the axis
    return ax
n_walks = 10
n_steps = 100