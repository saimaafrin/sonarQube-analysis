
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def task_func(text_dict, word_keys, top_k=2):
    if top_k < 0:
        raise ValueError("top_k must be a non-negative integer")

    # Calculate the frequency of the provided words in the dictionary
    word_freqs = Counter(word_keys)
    for word in text_dict:
        if word in word_keys:
            word_freqs[word] += 1

    # Create a bar chart of the frequencies
    ax = plt.bar(word_freqs.keys(), word_freqs.values())

    # Get the top_k most common words and their frequencies
    top_words = word_freqs.most_common(top_k)

    # Create a dictionary containing the top_k most common words and their frequencies
    top_k_words = {word: freq for word, freq in top_words}

    return ax, top_k_words