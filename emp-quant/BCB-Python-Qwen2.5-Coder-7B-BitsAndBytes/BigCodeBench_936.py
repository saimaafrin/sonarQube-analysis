
import numpy as np
import matplotlib.pyplot as plt
import string

# Constants
ALPHABET = list(string.ascii_lowercase)

def task_func(word):
    # Create an array to store the positions of each letter in the word
    positions = np.zeros(len(word))
    
    # Map each letter in the word to its position in the alphabet
    for i, char in enumerate(word):
        if char in ALPHABET:
            positions[i] = ALPHABET.index(char) + 1
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(range(len(word)), positions, tick_label=word)
    
    return ax