import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
def task_func(text_dict, word_keys, top_k=2):
    if top_k < 0:
        raise ValueError("top_k must be a non-negative integer")
    
    # Create a Counter object from the text_dict
    word_counter = Counter(text_dict)
    
    # Calculate the frequency of the provided words
    word_frequencies = {word: word_counter.get(word, 0) for word in word_keys}
    
    # Get the top_k most common words and their frequencies
    top_words = word_counter.most_common(top_k)
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar([word for word, freq in top_words], [freq for word, freq in top_words])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequencies')
    ax.set_title('Top {} Most Common Words'.format(top_k))
    
    return ax, dict(word_frequencies)
text_dict = {'apple': 10, 'banana': 5, 'cherry': 8, 'date': 3, 'elderberry': 12}
word_keys = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']