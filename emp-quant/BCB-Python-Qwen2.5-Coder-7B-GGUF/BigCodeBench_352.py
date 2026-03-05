
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def task_func(text_dict, word_keys, top_k=2):
    if top_k < 0:
        raise ValueError("top_k must be a non-negative integer")
    
    # Calculate the frequency of the provided words in the dictionary
    word_frequencies = {word: text_dict.get(word, 0) for word in word_keys}
    
    # Get the top_k most common words from the text_dict
    top_words = Counter(text_dict).most_common(top_k)
    
    # Create a bar chart displaying the frequencies
    fig, ax = plt.subplots()
    ax.bar([word[0] for word in top_words], [word[1] for word in top_words])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequencies')
    ax.set_title('Top {} Most Common Words'.format(top_k))
    
    return ax, dict(word_frequencies)