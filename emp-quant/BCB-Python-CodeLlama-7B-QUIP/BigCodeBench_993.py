
import re
from scipy.stats import gaussian_kde
from scipy import linalg
import matplotlib.pyplot as plt

def task_func(text):
    # Calculate the word lengths
    word_lengths = [len(word) for word in re.split(r'\W', text) if len(word) > 0]

    # Calculate the histogram of word lengths
    hist, bins = np.histogram(word_lengths, bins=50)

    # Calculate the KDE of word lengths
    kde = gaussian_kde(word_lengths)

    # Plot the histogram and KDE
    fig, ax = plt.subplots()
    ax.hist(bins, hist, label='Histogram')
    ax.plot(kde, label='KDE')
    ax.set_xlabel('Word length')
    ax.set_ylabel('Frequency')
    ax.legend()
    return ax