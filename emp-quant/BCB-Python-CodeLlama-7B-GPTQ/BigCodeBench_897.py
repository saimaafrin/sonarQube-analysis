import numpy as np
import matplotlib.pyplot as plt
import random
NUMBERS = list(range(1, 7))
def task_func(rolls, seed=None):
    """
    Simulate a number of dice rolls, calculate the frequency of each result, and return both the frequency array and a histogram of the results.
    """
    # Set random seed for reproducibility
    if seed is not None:
        random.seed(seed)

    # Simulate rolls
    rolls = [random.choice(NUMBERS) for _ in range(rolls)]

    # Calculate frequency
    freq = np.bincount(rolls)

    # Create histogram
    fig, ax = plt.subplots()
    ax.bar(NUMBERS, freq)
    ax.set_xlabel("Dice Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Dice Rolls")

    return freq, ax