import numpy as np
import matplotlib.pyplot as plt
import string
ALPHABET = list(string.ascii_lowercase)
def task_func(word):
    # Create a dictionary to map each letter to its position in the alphabet
    letter_positions = {letter: idx + 1 for idx, letter in enumerate(ALPHABET)}
    
    # Extract the positions of the letters in the given word
    positions = [letter_positions[letter] for letter in word if letter in letter_positions]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(range(len(positions)), positions, tick_label=word)
    
    # Set labels and title
    ax.set_xlabel('Letters')
    ax.set_ylabel('Positions in Alphabet')
    ax.set_title('Bar Chart of Letter Positions')
    
    return ax