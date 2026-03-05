
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(n_walks, n_steps, seed=None):
    # Check for valid input
    if n_walks <= 0 or n_steps <= 0:
        raise ValueError("Invalid input")

    # Generate walks
    walks = [np.random.rand(n_steps, 2) for _ in range(n_walks)]

    # Plot walks
    fig, ax = plt.subplots()
    colors = itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
    for i, walk in enumerate(walks):
        ax.plot(walk[:, 0], walk[:, 1], color=next(colors))

    return ax