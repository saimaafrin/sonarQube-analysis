
import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

def task_func(example_str, top_n=30):
    # Remove all words enclosed in square brackets
    pattern = re.compile(r'\[.*?\]')
    example_str = re.sub(pattern, '', example_str)

    # Tokenize the remaining words
    words = re.split(r'\W+', example_str)

    # Create a frequency distribution of the words
    freq_dist = FreqDist(words)

    # Plot the frequency distribution
    fig, ax = plt.subplots()
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency Distribution of Words')
    ax.plot(freq_dist.keys(), freq_dist.values())

    # Get the top_n most common words
    top_words = freq_dist.most_common(top_n)

    # Return the top_n most common words and their frequencies
    return top_words