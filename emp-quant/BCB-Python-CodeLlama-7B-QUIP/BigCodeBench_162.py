
import re
import matplotlib.pyplot as plt
import numpy as np

def task_func(text, rwidth=0.8):
    # Remove all punctuation and digits from the text
    text = re.sub(r'[^a-zA-Z]', '', text)

    # Tokenize the text into individual words
    words = re.split(r'\W+', text)

    # Create a histogram of word lengths
    word_lengths = [len(word) for word in words]
    n_bins = int(np.max(word_lengths) + 1)
    hist, bins = np.histogram(word_lengths, bins=n_bins)

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(bins[:-1], hist, align='mid', rwidth=rwidth)
    ax.set_xlabel('Word length')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of word lengths')
    return ax