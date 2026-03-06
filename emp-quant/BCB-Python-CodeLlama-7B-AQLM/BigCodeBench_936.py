import numpy as np
import matplotlib.pyplot as plt
import string
ALPHABET = list(string.ascii_lowercase)
def task_func(word):
    """
    Draws a bar chart representing the positions of each letter in the given word 
    within the English alphabet using numpy and matplotlib.pyplot.
    
    Parameters:
    word (str): The word whose letters' positions will be plotted. 
                Should contain only lowercase alphabetic characters.
                
    Returns:
    Axes: A matplotlib.axes._axes.Axes object representing the generated plot.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    
    Constants:
    - ALPHABET: A list containing all lowercase letters of the English alphabet.
    
    Examples:
    >>> ax = task_func('abc')
    >>> ax = task_func('hello')
    
    Note: 
    The function uses the index of each letter in the English alphabet to represent its position.
    For example, 'a' will be represented by 1, 'b' by 2, and so on.
    """
    # Check if the word contains only lowercase alphabetic characters
    if not all(c.isalpha() and c.islower() for c in word):
        raise ValueError('The word should contain only lowercase alphabetic characters.')
    
    # Get the positions of each letter in the word
    positions = [ALPHABET.index(c) for c in word]
    
    # Create a bar chart
    ax = plt.bar(positions, height=1, width=0.8)
    
    # Set the x-axis labels
    ax.set_xticks(positions)
    ax.set_xticklabels(word)
    
    # Set the y-axis labels
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['0', '1'])
    
    # Set the title
    ax.set_title('Positions of letters in the word')
    
    # Set the x-axis label
    ax.set_xlabel('Letter')
    
    # Set the y-axis label
    ax.set_ylabel('Position')
    
    # Set the plot's size
    plt.rcParams['figure.figsize'] = (10, 5)
    
    # Return the plot
    return ax