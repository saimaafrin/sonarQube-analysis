
import numpy as np
import matplotlib.pyplot as plt
import string
# Constants
ALPHABET = list(string.ascii_lowercase)
def task_func(word):
    # Create a numpy array with the positions of each letter in the word
    positions = np.array([ALPHABET.index(letter) for letter in word])
    # Create a bar chart with the positions of each letter
    ax = plt.bar(positions, width=0.5)
    # Set the x-axis labels to the letters of the alphabet
    ax.set_xticks(np.arange(len(ALPHABET)))
    ax.set_xticklabels(ALPHABET)
    # Set the y-axis label to the number of occurrences of each letter
    ax.set_ylabel('Number of occurrences')
    # Set the title of the plot
    ax.set_title('Letter positions in the word')
    # Return the axes object
    return ax