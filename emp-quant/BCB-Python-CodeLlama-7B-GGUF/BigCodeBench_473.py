
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(n_walks, n_steps, seed=None):
    # Check for valid input
    if n_walks < 1 or n_steps < 1:
        raise ValueError("n_walks and n_steps must be positive integers")

    # Generate random walks
    walks = np.random.randint(0, n_steps, size=(n_walks, n_steps))

    # Plot walks
    ax = plt.gca()
    for i, walk in enumerate(walks):
        ax.plot(walk, color=next(itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k'])))

    # Set axis labels
    ax.set_xlabel("Step")
    ax.set_ylabel("Position")
    ax.set_title("Random Walks")

    return ax