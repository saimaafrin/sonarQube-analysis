
import re
import matplotlib.pyplot as plt
import numpy as np

def task_func(text, rwidth=0.8):
    # Split the text into words using regex to handle different delimiters
    words = re.findall(r'\b\w+\b', text)
    
    if not words:
        return None  # Return None if no words are found
    
    # Calculate the length of each word
    word_lengths = [len(word) for word in words]
    
    # Create a figure and an axes object
    fig, ax = plt.subplots()
    
    # Generate the histogram
    n, bins, patches = ax.hist(word_lengths, bins='auto', rwidth=rwidth)
    
    # Set labels and title
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Word Lengths')
    
    # Return the axes object
    return ax