import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
def task_func(example_str, top_n=30):
    """
    Extract all texts that are not enclosed in square brackets from the given string and plot 
    a frequency distribution of the words. Also return the top_n most common words in the frequency distribution
    as a dictionary.

    Parameters:
    - example_str (str): The input string.
    - top_n (int, Optional): The number of most common words to display in the frequency distribution plot. Default is 30.

    Returns:
    - Axes: A matplotlib Axes object representing the frequency distribution plot.
    - dict: A dictionary containing the top_n most common words and their frequencies.

    Requirements:
    - re
    - nltk.probability.FreqDist
    - matplotlib.pyplot

    Example:
    >>> ax, top_n_words = task_func("Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]")
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    # Extract all words that are not enclosed in square brackets
    words = re.findall(r'\[.*?\]|\w+', example_str)
    words = [word for word in words if not word.startswith('[')]

    # Create a frequency distribution of the words
    freq_dist = FreqDist(words)

    # Create a frequency distribution plot
    ax = freq_dist.plot(100, cumulative=False)

    # Return the top_n most common words and their frequencies
    top_n_words = freq_dist.most_common(top_n)
    return ax, top_n_words