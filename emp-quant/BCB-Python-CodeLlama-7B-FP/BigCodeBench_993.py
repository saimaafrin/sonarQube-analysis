import re
from scipy.stats import gaussian_kde
from scipy import linalg
import matplotlib.pyplot as plt
def task_func(text):
    """
    This function takes a text input, calculates the lengths of the words, and visualizes the distribution of word lengths using a histogram and a KDE curve (if applicable) on a matplotlib subplot.
    The function should output with:
        matplotlib.axes._axes.Axes: An Axes object showing the histogram and optionally the KDE
        plot of word lengths. This visual representation helps in
        understanding the distribution of word lengths in the given text.
    """
    # Calculate the lengths of the words in the text
    words = re.split(r'\W+', text)
    word_lengths = [len(word) for word in words]

    # Calculate the histogram of word lengths
    hist, bins = np.histogram(word_lengths, bins=20)

    # Calculate the KDE of word lengths
    kde = gaussian_kde(word_lengths)

    # Create a subplot for the histogram and KDE
    fig, ax = plt.subplots()

    # Plot the histogram
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0])

    # Plot the KDE
    ax.plot(bins, kde(bins), color='red')

    # Set the title and labels
    ax.set_title('Distribution of Word Lengths')
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Frequency')

    # Return the Axes object
    return ax
text = 'This is a sample text with some words of varying lengths.'