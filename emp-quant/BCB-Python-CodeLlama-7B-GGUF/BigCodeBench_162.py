
import re
import matplotlib.pyplot as plt
import numpy as np

def task_func(text, rwidth=0.8):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^a-zA-Z]', '', text.lower())

    # Split text into individual words
    words = text.split()

    # Calculate word lengths
    lengths = [len(word) for word in words]

    # Create histogram of word lengths
    n_bins = 10
    hist, bin_edges = np.histogram(lengths, bins=n_bins)

    # Normalize histogram
    hist = hist / len(lengths)

    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot histogram
    ax.bar(bin_edges[:-1], hist, width=rwidth, align='edge')

    # Set axis labels
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Frequency')

    # Set title
    ax.set_title('Histogram of Word Lengths')

    return ax