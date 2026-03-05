import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
def task_func(example_str, top_n=30):
    """
    Extract all texts that are not enclosed in square brackets from the given string and plot a frequency distribution of the words.
    Also return the top_n most common words in the frequency distribution as a dictionary.
    """
    # Extract all texts that are not enclosed in square brackets from the given string
    texts = re.findall(r'\[.*?\]', example_str)
    # Create a frequency distribution of the words
    freq_dist = FreqDist(texts)
    # Plot the frequency distribution
    ax = freq_dist.plot(kind='bar')
    # Return the top_n most common words in the frequency distribution as a dictionary
    return ax, freq_dist.most_common(top_n)
example_str = 'This is an example string [with enclosed text] and some more text [with enclosed text]'