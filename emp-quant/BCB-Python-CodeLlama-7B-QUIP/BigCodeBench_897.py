
import numpy as np
import matplotlib.pyplot as plt
import random
# Constants
NUMBERS = list(range(1, 7))  # Adjusting for dice rolls (1 to 6)
def task_func(rolls, seed=None):
    # Initialize the frequency array
    freq = np.zeros(6)
    # Initialize the histogram
    hist = plt.figure()
    # Generate the random numbers
    if seed:
        random.seed(seed)
    for i in range(rolls):
        freq[random.randint(1, 6)] += 1
    # Plot the histogram
    plt.hist(freq, bins=6, label="Histogram of Dice Rolls")
    plt.xlabel("Dice Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of Dice Rolls")
    plt.show()
    return freq, hist