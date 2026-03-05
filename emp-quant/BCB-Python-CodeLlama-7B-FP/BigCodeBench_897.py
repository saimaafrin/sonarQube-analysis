import numpy as np
import matplotlib.pyplot as plt
import random
NUMBERS = list(range(1, 7))
def task_func(rolls, seed=None):
    """
    Simulate a number of dice rolls, calculate the frequency of each result, and return both the frequency array and a histogram of the results.
    """
    # Set random seed if provided
    if seed is not None:
        random.seed(seed)

    # Initialize frequency array
    freq = np.zeros(len(NUMBERS))

    # Simulate rolls
    for _ in range(rolls):
        # Roll a die
        roll = random.choice(NUMBERS)

        # Increment frequency
        freq[roll - 1] += 1

    # Create histogram
    fig, ax = plt.subplots()
    ax.bar(NUMBERS, freq, label='Histogram of Dice Rolls')
    ax.set_xlabel('Dice Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Dice Rolls')

    # Return frequency array and histogram
    return freq, ax