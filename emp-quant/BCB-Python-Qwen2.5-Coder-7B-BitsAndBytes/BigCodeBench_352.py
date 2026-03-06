
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def task_func(text_dict, word_keys, top_k=2):
    if top_k < 0:
        raise ValueError("top_k must be a non-negative integer")
    
    # Create a Counter object from the text_dict
    word_counter = Counter(text_dict)
    
    # Calculate the frequency of the provided words
    word_frequencies = {word: word_counter[word] for word in word_keys}
    
    # Get the top_k most common words
    top_words = word_counter.most_common(top_k)
    
    # Create a DataFrame for plotting
    df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])
    
    # Plotting the bar chart
    ax = df.plot(kind='bar', x='Word', y='Frequency', legend=False)
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequencies')
    ax.set_title('Top {} Most Common Words'.format(top_k))
    
    return ax, word_frequencies