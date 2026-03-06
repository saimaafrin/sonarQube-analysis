
import re
import matplotlib.pyplot as plt
import numpy as np

def task_func(text, rwidth=0.8):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Split the text into individual words
    words = text.split()

    # Calculate the length of each word
    lengths = [len(word) for word in words]

    # Create a histogram of word lengths
    hist, bins = np.histogram(lengths, bins=range(0, 100, 10))

    # Normalize the histogram
    hist = hist / len(words)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the histogram
    ax.bar(bins[:-1], hist, width=rwidth)

    # Set the axis labels
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Frequency')

    # Return the Axes object
    return ax