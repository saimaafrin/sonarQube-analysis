
import re
import matplotlib.pyplot as plt
import numpy as np

def task_func(text, rwidth=0.8):
    # Split the text into words using regular expression
    words = re.findall(r'\b\w+\b', text)
    
    # If there are no words, return an empty plot
    if not words:
        fig, ax = plt.subplots()
        return ax
    
    # Calculate the lengths of the words
    word_lengths = [len(word) for word in words]
    
    # Create a histogram of word lengths
    fig, ax = plt.subplots()
    ax.hist(word_lengths, bins='auto', rwidth=rwidth, edgecolor='black')
    
    # Set the title and labels
    ax.set_title('Word Length Distribution')
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object
    return ax