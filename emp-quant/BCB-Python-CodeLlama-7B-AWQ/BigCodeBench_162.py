import re
import matplotlib.pyplot as plt
import numpy as np
def task_func(text, rwidth=0.8):
    """
    Analyzes and visualizes the distribution of word lengths in a text.
    The function generates a histogram subplot, which facilitates the understanding of how word lengths vary within the provided text.
    Note that: If there are no words in the input text, or all words are filtered out, the histogram will be empty as no bins will be created.
    """
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^a-zA-Z]', '', text.lower())

    # Split text into individual words
    words = text.split()

    # Create a histogram of word lengths
    word_lengths = [len(word) for word in words]
    n_bins = int(np.sqrt(len(word_lengths)))
    hist, bin_edges = np.histogram(word_lengths, bins=n_bins)

    # Normalize histogram
    hist = hist / len(word_lengths)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the histogram
    ax.bar(bin_edges[:-1], hist, width=rwidth)

    # Set axis labels
    ax.set_xlabel('Word length')
    ax.set_ylabel('Frequency')

    # Return the Axes object
    return ax
text = "This is a sample text with some words of varying lengths."