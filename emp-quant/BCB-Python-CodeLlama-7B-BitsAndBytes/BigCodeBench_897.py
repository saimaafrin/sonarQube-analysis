
import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
NUMBERS = list(range(1, 7))  # Adjusting for dice rolls (1 to 6)

def task_func(rolls, seed=None):
    # Initialize an array to store the frequency of each outcome
    freq = np.zeros(len(NUMBERS))

    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Simulate the dice rolls and update the frequency array
    for _ in range(rolls):
        freq[random.choice(NUMBERS)] += 1

    # Create a histogram of the results
    fig, ax = plt.subplots()
    ax.bar(NUMBERS, freq, width=0.8)
    ax.set_title("Histogram of Dice Rolls")
    ax.set_xlabel("Dice Value")
    ax.set_ylabel("Frequency")
    ax.set_xticks(NUMBERS)
    ax.set_xticklabels(NUMBERS)

    return freq, ax