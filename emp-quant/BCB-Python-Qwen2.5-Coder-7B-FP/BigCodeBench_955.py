import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter
def task_func(mystrings, text):
    if not text:
        raise ValueError("Input text is empty")
    
    # Convert text to lowercase and replace spaces with underscores
    modified_text = re.sub(r'\s+', '_', text.lower())
    
    # Split the modified text into words
    words = modified_text.split('_')
    
    # Count the frequency of each unique word
    word_counts = Counter(words)
    
    # Extract words and their frequencies
    words = list(word_counts.keys())
    frequencies = list(word_counts.values())
    
    # Create a figure and axis for the plot
    fig, ax = plt.subplots()
    
    # Plot the frequency of each unique word
    ax.bar(words, frequencies)
    
    # Set the title and labels for the plot
    ax.set_title('Word Frequency')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    
    # Rotate the x-axis labels for better readability
    ax.set_xticklabels(words, rotation=45)
    
    # Return the Axes object of the plot
    return ax