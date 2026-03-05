
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

def task_func(mystrings, text):
    if not text:
        raise ValueError("Input text is empty")

    # Replace spaces with underscores
    text = re.sub(r"\s+", "_", text)

    # Count the frequency of each unique word
    counts = Counter(text.split())

    # Create a bar plot of the frequency of each unique word
    ax = plt.bar(counts.keys(), counts.values())

    # Set the x-axis labels to the unique words
    ax.set_xticks(counts.keys())
    ax.set_xticklabels(counts.keys(), rotation=90)

    # Set the y-axis label to the frequency of each unique word
    ax.set_ylabel("Frequency")

    return ax