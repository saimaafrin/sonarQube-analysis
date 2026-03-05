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
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Split the text into individual words
    words = text.split()

    # Create a histogram of word lengths
    hist, bins = np.histogram(words, bins=np.arange(0, 100, 1))

    # Normalize the histogram
    hist = hist / np.sum(hist)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the histogram
    ax.bar(bins[:-1], hist, width=rwidth, align='edge')

    # Set the x-axis label
    ax.set_xlabel('Word length')

    # Set the y-axis label
    ax.set_ylabel('Frequency')

    # Set the title
    ax.set_title('Word length distribution')

    # Return the Axes object
    return ax
text = 'This is a sample text with some words of varying lengths.'