
import numpy as np
import matplotlib.pyplot as plt
import string

# Constants
ALPHABET = list(string.ascii_lowercase)

def task_func(word):
    # Create a dictionary to map each letter to its position in the alphabet
    letter_positions = {letter: index + 1 for index, letter in enumerate(ALPHABET)}
    
    # Extract the positions of the letters in the given word
    positions = [letter_positions[letter] for letter in word if letter in ALPHABET]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(range(len(positions)), positions, tick_label=word)
    
    # Set the title and labels
    ax.set_title('Letter Positions in Alphabet')
    ax.set_xlabel('Letters')
    ax.set_ylabel('Positions')
    
    # Return the Axes object
    return ax