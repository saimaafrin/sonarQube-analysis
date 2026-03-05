
import numpy as np
import matplotlib.pyplot as plt
import string
# Constants
ALPHABET = list(string.ascii_lowercase)
def task_func(word):
    # Create a numpy array with the positions of each letter in the word
    positions = np.array([ALPHABET.index(letter) for letter in word])
    # Create a bar chart with the positions
    plt.bar(positions, np.ones(len(positions)))
    # Show the plot
    plt.show()
    return positions