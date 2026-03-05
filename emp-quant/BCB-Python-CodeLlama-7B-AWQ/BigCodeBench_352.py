import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
def task_func(text_dict, word_keys, top_k=2):
    """
    Calculate the frequency of certain words in a text dictionary and return a bar chart's Axes object and a dictionary containing the frequencies of the top_k most common words in text_dict.
    The function takes a dictionary containing word frequencies and a list of words. It calculates the frequency of the provided words in the dictionary and returns the Axes object of the bar chart displaying the frequencies along with the top_k most common words and their frequencies as a dictionary. If a word in word_keys is not present in text_dict, its frequency is considered to be 0.
    The function should raise the exception for:
        ValueError: If top_k is a negative integer.
    The function should output with:
        matplotlib.axes._axes.Axes: Axes object of the bar chart displaying the frequencies.
        dict: Dictionary containing the frequencies of the top_k most common words. Key is the word and value is
        its frequency.
    """
    if top_k < 0:
        raise ValueError("top_k must be a non-negative integer")

    # Calculate the frequency of the provided words in the dictionary
    word_freqs = Counter(text_dict)
    word_freqs = {word: word_freqs[word] for word in word_keys}

    # Create a bar chart of the frequencies
    fig, ax = plt.subplots()
    ax.bar(word_freqs.keys(), word_freqs.values())
    ax.set_title("Word Frequencies")
    ax.set_xlabel("Word")
    ax.set_ylabel("Frequency")

    # Get the top_k most common words and their frequencies
    top_k_words = sorted(word_freqs.items(), key=lambda x: x[1], reverse=True)[:top_k]

    # Return the Axes object and the top_k most common words and their frequencies as a dictionary
    return ax, {word: freq for word, freq in top_k_words}
text_dict = {"apple": 5, "banana": 3, "cherry": 2, "date": 1, "elderberry": 4}
word_keys = ["apple", "banana", "cherry"]