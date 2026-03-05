
import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
NUMBERS = list(range(1, 7))  # Adjusting for dice rolls (1 to 6)

def task_func(rolls, seed=None):
    # Seed the random number generator for reproducibility
    if seed is not None:
        random.seed(seed)

    # Initialize a frequency array with zeros
    frequency = np.zeros(6)

    # Simulate the dice rolls
    for _ in range(rolls):
        roll = random.randint(1, 6)
        frequency[roll - 1] += 1

    # Create the histogram
    fig, ax = plt.subplots()
    ax.bar(NUMBERS, frequency, tick_label=NUMBERS, edgecolor='black')
    ax.set_title('Histogram of Dice Rolls')
    ax.set_xlabel('Dice Value')
    ax.set_ylabel('Frequency')

    # Return the frequency array and the axes object
    return frequency, ax