
import re
from scipy.stats import gaussian_kde
from scipy import linalg
import matplotlib.pyplot as plt

def task_func(text):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)
    
    # Calculate the lengths of the words
    word_lengths = [len(word) for word in words]
    
    # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    
    # Plot the histogram of word lengths
    ax.hist(word_lengths, bins=range(min(word_lengths), max(word_lengths) + 2), edgecolor='k')
    
    # Plot the KDE curve of word lengths
    kde = gaussian_kde(word_lengths)
    x = range(min(word_lengths), max(word_lengths) + 1)
    ax.plot(x, kde(x), 'r--')
    
    # Set the title and labels
    ax.set_title('Word Length Distribution')
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object
    return ax