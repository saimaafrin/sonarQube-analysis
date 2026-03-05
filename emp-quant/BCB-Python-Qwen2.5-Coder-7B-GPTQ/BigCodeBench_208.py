import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def task_func(elements, seed=0):
    """
    Generate and draw a random sequence of 'elements' number of steps.
    The steps are either -1 or 1, and the sequence is plotted as a random walk.
    Returns the descriptive statistics of the random walk and the plot of the random walk.
    
    Parameters:
    elements (int): The number of steps in the random walk.
    seed (int): The seed for the random number generator.
    
    Returns:
    dict: A dictionary containing the descriptive statistics of the random walk.
    matplotlib.axes.Axes: The Axes object with the plotted random walk.
    """
    if not isinstance(elements, int) or elements <= 0:
        raise ValueError("elements must be a positive integer")
    
    np.random.seed(seed)
    steps = np.random.choice([-1, 1], size=elements)
    random_walk = np.cumsum(steps)
    
    # Calculate descriptive statistics
    stats = {
        'count': len(random_walk),
        'mean': np.mean(random_walk),
        'std': np.std(random_walk),
        'min': np.min(random_walk),
        '5th_percentile': np.percentile(random_walk, 5),
        '25th_percentile': np.percentile(random_walk, 25),
        'median': np.median(random_walk),
        '75th_percentile': np.percentile(random_walk, 75),
        '95th_percentile': np.percentile(random_walk, 95),
        'max': np.max(random_walk)
    }
    
    # Plot the random walk
    fig, ax = plt.subplots()
    ax.plot(random_walk)
    ax.set_title('Random Walk')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Position')
    
    return stats, ax