
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(elements, seed=0):
    if not isinstance(elements, int) or elements <= 0:
        raise ValueError("elements must be a positive integer")
    
    np.random.seed(seed)
    steps = np.random.choice([-1, 1], size=elements)
    random_walk = np.cumsum(steps)
    
    stats = {
        'count': len(random_walk),
        'mean': random_walk.mean(),
        'std': random_walk.std(),
        'min': random_walk.min(),
        '5th_percentile': np.percentile(random_walk, 5),
        '25th_percentile': np.percentile(random_walk, 25),
        'median': np.median(random_walk),
        '75th_percentile': np.percentile(random_walk, 75),
        '95th_percentile': np.percentile(random_walk, 95),
        'max': random_walk.max()
    }
    
    fig, ax = plt.subplots()
    ax.plot(random_walk)
    ax.set_title('Random Walk')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Position')
    
    return stats, ax