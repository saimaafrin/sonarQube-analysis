
import collections
import matplotlib.pyplot as plt
import pandas as pd
# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
def task_func(sentences_dict, word_keys):
    # Create a dictionary to store the word frequencies
    word_freqs = collections.defaultdict(int)
    # Loop through each sentence in the dictionary
    for sentence in sentences_dict:
        # Tokenize the sentence
        tokens = sentence.split()
        # Loop through each word in the sentence
        for word in tokens:
            # Check if the word is in the list of target words
            if word in word_keys:
                # Increment the frequency of the word
                word_freqs[word] += 1
    # Create a bar chart
    plt.bar(word_freqs.keys(), word_freqs.values())
    plt.show()
    return plt.axes