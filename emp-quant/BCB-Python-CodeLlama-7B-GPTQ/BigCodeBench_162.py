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

    # Filter out words that are too short or too long
    words = [word for word in words if len(word) > 2 and len(word) < 10]

    # Create a histogram of word lengths
    hist, bins = np.histogram(words, bins=10, range=(2, 10))

    # Normalize the histogram
    hist = hist / len(words)

    # Create a bar plot of the histogram
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0])
    ax.set_xlabel('Word length')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Word Lengths')

    return ax
text = 'This is a sample text with some words that are too long and some that are too short.'