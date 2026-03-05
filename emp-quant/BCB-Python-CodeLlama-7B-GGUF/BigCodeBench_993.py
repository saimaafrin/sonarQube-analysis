
import re
from scipy.stats import gaussian_kde
from scipy import linalg
import matplotlib.pyplot as plt

def task_func(text):
    # Calculate the lengths of the words in the text
    words = re.split(r'\W+', text)
    word_lengths = [len(word) for word in words]

    # Calculate the histogram of word lengths
    hist, bin_edges = np.histogram(word_lengths, bins=20)

    # Calculate the KDE of word lengths
    kde = gaussian_kde(word_lengths)
    x = np.linspace(min(word_lengths), max(word_lengths), 100)
    y = kde(x)

    # Plot the histogram and KDE
    fig, ax = plt.subplots()
    ax.bar(bin_edges[:-1], hist, width=bin_edges[1] - bin_edges[0])
    ax.plot(x, y)
    ax.set_xlabel('Word length')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of word lengths')
    return fig