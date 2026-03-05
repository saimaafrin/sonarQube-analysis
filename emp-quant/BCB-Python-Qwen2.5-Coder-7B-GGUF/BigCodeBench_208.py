
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(elements, seed=0):
    if not isinstance(elements, int) or elements <= 0:
        raise ValueError("elements must be a positive integer")
    
    np.random.seed(seed)
    random_walk = np.cumsum(np.random.choice([-1, 1], size=elements))
    
    descriptive_stats = {
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
    
    fig, ax = plt.subplots()
    ax.plot(random_walk)
    ax.set_title('Random Walk')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Position')
    
    return descriptive_stats, ax