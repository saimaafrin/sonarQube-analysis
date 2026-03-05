
import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
NUMBERS = list(range(1, 7))  # Adjusting for dice rolls (1 to 6)

def task_func(rolls, seed=None):
    """
    Simulate a number of dice rolls, calculate the frequency of each result, and return both the frequency array and a histogram of the results.

    Parameters
    ----------
    rolls : int
        Number of dice rolls to simulate.
    seed : int, optional
        Random seed to use for reproducibility.

    Returns
    -------
    tuple
        A tuple containing:

        np.array
            A numpy array with the frequency of each outcome.
        matplotlib.Axes
            Axes object representing the histogram.
    """
    # Set random seed for reproducibility
    if seed is not None:
        random.seed(seed)

    # Initialize frequency array
    freq = np.zeros(len(NUMBERS))

    # Simulate rolls and update frequency array
    for i in range(rolls):
        freq[random.choice(NUMBERS)] += 1

    # Create histogram
    fig, ax = plt.subplots()
    ax.bar(NUMBERS, freq)
    ax.set_xlabel("Dice Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Dice Rolls")

    return freq, ax