import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter
def task_func(mystrings, text):
    """
    Replace spaces in given words with underscores, then plots the frequency of each unique word.
    """
    if not text:
        raise ValueError("Input text is empty.")

    # Replace spaces with underscores
    text = re.sub(r"\s+", "_", text)

    # Count the frequency of each unique word
    counts = Counter(text.split())

    # Create a bar plot of the word frequencies
    ax = plt.bar(counts.keys(), counts.values())

    # Set the x-axis labels
    ax.set_xticks(counts.keys())
    ax.set_xticklabels(counts.keys(), rotation=90)

    # Set the y-axis label
    ax.set_ylabel("Frequency")

    return ax
mystrings = ["hello world", "hello world", "hello world", "goodbye world"]
text = "hello world goodbye world"