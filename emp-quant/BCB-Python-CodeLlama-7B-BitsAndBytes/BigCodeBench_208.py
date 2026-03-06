
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(elements, seed=0):
    if elements <= 0:
        raise ValueError("elements must be a positive integer")

    # Generate a random sequence of elements
    sequence = np.random.choice([-1, 1], size=elements, p=[0.5, 0.5])

    # Calculate the descriptive statistics of the random walk
    stats = pd.Series(sequence).describe()

    # Plot the random walk
    fig, ax = plt.subplots()
    ax.plot(sequence)
    ax.set_xlabel("Step")
    ax.set_ylabel("Value")
    ax.set_title("Random Walk")

    return stats, fig