
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(elements, seed=0):
    if elements <= 0:
        raise ValueError("elements must be a positive integer")

    np.random.seed(seed)
    x = np.random.randint(-1, 2, size=elements)

    # Calculate descriptive statistics
    count = len(x)
    mean = np.mean(x)
    std = np.std(x)
    min = np.min(x)
    p5 = np.percentile(x, 5)
    p25 = np.percentile(x, 25)
    median = np.median(x)
    p75 = np.percentile(x, 75)
    p95 = np.percentile(x, 95)
    max = np.max(x)

    # Plot the random walk
    fig, ax = plt.subplots()
    ax.plot(x)
    ax.set_xlabel("Step")
    ax.set_ylabel("Value")
    ax.set_title("Random Walk")
    plt.show()

    # Return the descriptive statistics and the plot
    return {
        "count": count,
        "mean": mean,
        "std": std,
        "min": min,
        "5th percentile": p5,
        "25th percentile": p25,
        "median": median,
        "75th percentile": p75,
        "95th percentile": p95,
        "max": max
    }, ax