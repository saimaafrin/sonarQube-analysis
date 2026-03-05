
import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

def task_func(example_str, top_n=30):
    # Extract texts that are not enclosed in square brackets
    texts = re.findall(r'\[.*\]|[^[\]]+', example_str)
    # Join all texts and split into words
    all_words = ' '.join(texts).split()
    # Filter out non-alphabetic words
    words = [word for word in all_words if word.isalpha()]
    # Create a frequency distribution
    freq_dist = FreqDist(words)
    # Plot the frequency distribution
    freq_dist.plot(30, cumulative=False)
    plt.show()
    # Get the top_n most common words
    top_words = freq_dist.most_common(top_n)
    # Convert the list of tuples to a dictionary
    top_words_dict = dict(top_words)
    return plt.gca(), top_words_dict