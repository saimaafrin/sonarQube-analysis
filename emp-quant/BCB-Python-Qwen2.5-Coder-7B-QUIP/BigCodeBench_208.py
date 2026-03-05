
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(elements, seed=0):
    if not isinstance(elements, int) or elements <= 0:
        raise ValueError("elements must be a positive integer")
    
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate the random walk
    steps = np.random.choice([-1, 1], size=elements)
    random_walk = np.cumsum(steps)
    
    # Calculate descriptive statistics
    stats = {
        'count': len(random_walk),
        'mean': np.mean(random_walk),
        'std_dev': np.std(random_walk),
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
    ax.plot(random_walk, '-o')
    ax.set_title('Random Walk')
    ax.set_xlabel('Step')
    ax.set_ylabel('Position')
    
    return stats, ax