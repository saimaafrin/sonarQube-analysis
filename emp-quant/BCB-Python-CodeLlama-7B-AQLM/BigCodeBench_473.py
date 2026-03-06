import numpy as np
import matplotlib.pyplot as plt
import itertools
def task_func(n_walks, n_steps, seed=None):
    """
    Create and plot `n_walks` number of random walks, each with `n_steps` steps.

    The function checks for valid n_walks and n_steps, then generates walks via numpy.
    Each walk is plotted in a different color cycling through a predefined set of colors:
    ['b', 'g', 'r', 'c', 'm', 'y', 'k'].

    Parameters:
    - n_walks (int): The number of random walks to be generated and plotted.
    - n_steps (int): The number of steps in each random walk.
    - seed (int, optional): Seed for random number generation. Default is None.

    Returns:
    - ax (plt.Axes): A Matplotlib Axes containing the plotted random walks.

    Requirements:
    - numpy
    - matplotlib
    - itertools

    Example:
    >>> ax = task_func(5, 100, seed=42)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(-20.0, 0, '−20'), Text(0.0, 0, '0'), Text(20.0, 0, '20'), Text(40.0, 0, '40'), Text(60.0, 0, '60'), Text(80.0, 0, '80'), Text(100.0, 0, '100'), Text(120.0, 0, '120')]
    """
    # Check for valid n_walks and n_steps
    if n_walks < 1:
        raise ValueError("n_walks must be a positive integer.")
    if n_steps < 1:
        raise ValueError("n_steps must be a positive integer.")

    # Generate walks
    walks = np.random.randint(low=0, high=100, size=(n_walks, n_steps))

    # Plot walks
    ax = plt.gca()
    ax.set_xlim([-20, 120])
    ax.set_ylim([-20, 120])
    ax.set_xticks(np.arange(-20, 120, 20))
    ax.set_yticks(np.arange(-20, 120, 20))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title("Random walks")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    colors = itertools.cycle(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
    for i in range(n_walks):
        ax.plot(walks[i], color=next(colors))
    return ax