
import numpy as np
import matplotlib.pyplot as plt
import string

# Constants
ALPHABET = list(string.ascii_lowercase)

def task_func(word):
    # Create a numpy array with the positions of each letter in the word
    letter_positions = np.array([ALPHABET.index(letter) for letter in word])

    # Create a bar chart with the positions of each letter
    fig, ax = plt.subplots()
    ax.bar(letter_positions, height=1, color='blue')
    ax.set_xticks(np.arange(len(ALPHABET)))
    ax.set_xticklabels(ALPHABET)
    ax.set_ylabel('Position in the English alphabet')
    ax.set_title('Positions of letters in the word')

    return ax