
import re
import matplotlib.pyplot as plt
import numpy as np

def task_func(text, rwidth=0.8):
    # Split the text into words using regular expression to handle different delimiters
    words = re.findall(r'\b\w+\b', text)
    
    # If no words are found, return an empty figure
    if not words:
        fig, ax = plt.subplots()
        return ax
    
    # Calculate the lengths of the words
    word_lengths = [len(word) for word in words]
    
    # Create a histogram of word lengths
    fig, ax = plt.subplots()
    ax.hist(word_lengths, bins=np.arange(1, max(word_lengths) + 2) - 0.5, rwidth=rwidth)
    
    # Set labels and title
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Word Lengths')
    
    return ax