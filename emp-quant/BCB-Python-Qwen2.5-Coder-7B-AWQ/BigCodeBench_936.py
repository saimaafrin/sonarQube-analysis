import numpy as np
import matplotlib.pyplot as plt
import string
ALPHABET = list(string.ascii_lowercase)
def task_func(word):
    # Initialize a dictionary to store the positions of each letter
    letter_positions = {}
    
    # Iterate over each letter in the word
    for index, letter in enumerate(word, start=1):
        # Check if the letter is in the alphabet
        if letter in ALPHABET:
            # Store the position of the letter
            letter_positions[letter] = index
    
    # Create a list of positions for plotting
    positions = [letter_positions.get(letter, 0) for letter in ALPHABET]
    
    # Create a numpy array of positions
    positions_array = np.array(positions)
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(ALPHABET, positions_array)
    
    # Set the title and labels
    ax.set_title('Letter Positions in Word')
    ax.set_xlabel('Letters')
    ax.set_ylabel('Positions')
    
    # Return the Axes object
    return ax