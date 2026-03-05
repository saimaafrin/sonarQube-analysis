
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

def task_func(mystrings, text):
    # Replace spaces with underscores
    text = re.sub(" ", "_", text)
    # Count the frequency of each unique word
    counts = Counter(text.split())
    # Sort the words by frequency
    sorted_words = sorted(counts.keys(), key=counts.get)
    # Plot the frequency of each unique word
    fig, ax = plt.subplots()
    ax.bar(sorted_words, counts.values(), color="blue")
    ax.set_xlabel("Word")
    ax.set_ylabel("Frequency")
    ax.set_title("Frequency of words in the text")
    return ax