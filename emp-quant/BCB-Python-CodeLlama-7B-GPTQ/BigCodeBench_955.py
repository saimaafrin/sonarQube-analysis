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

    # Create a list of unique words
    words = list(counts.keys())

    # Sort the list of unique words in alphabetical order
    words.sort()

    # Create a list of frequencies
    freqs = [counts[word] for word in words]

    # Create a bar plot
    ax = plt.bar(words, freqs)

    return ax
mystrings = ["hello world", "hello world", "hello world", "goodbye world"]
text = "hello world goodbye world"