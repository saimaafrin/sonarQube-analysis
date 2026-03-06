
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

def task_func(mystrings, text):
    if not text:
        raise ValueError("Input text is empty")

    # Replace spaces with underscores
    text = re.sub(r'\s+', '_', text)

    # Count the frequency of each unique word
    counts = Counter(text.split())

    # Create a bar plot of the frequency of each word
    ax = plt.bar(counts.keys(), counts.values())

    # Set the title and labels
    ax.set_title("Word Frequencies")
    ax.set_xlabel("Word")
    ax.set_ylabel("Frequency")

    return ax