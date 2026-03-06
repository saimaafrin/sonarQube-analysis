
import re
from scipy.stats import gaussian_kde
from scipy import linalg
import matplotlib.pyplot as plt

def task_func(text):
    # Split the text into individual words
    words = re.split(r'\W+', text)

    # Calculate the lengths of the words
    lengths = [len(word) for word in words]

    # Calculate the histogram of word lengths
    hist, bins = np.histogram(lengths, bins=20)

    # Calculate the KDE of word lengths
    kde = gaussian_kde(lengths)

    # Create a figure and subplot
    fig, ax = plt.subplots()

    # Plot the histogram of word lengths
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0])

    # Plot the KDE of word lengths
    ax.plot(bins[:-1], kde(bins[:-1]), color='red')

    # Set the title and labels
    ax.set_title('Word Length Distribution')
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Frequency')

    # Return the Axes object
    return ax