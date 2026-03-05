
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def task_func(text_dict, word_keys, top_k=2):
    # Check if top_k is a negative integer
    if top_k < 0:
        raise ValueError("top_k must be a non-negative integer")
    
    # Initialize a Counter for the word frequencies in text_dict
    word_counter = Counter(text_dict)
    
    # Calculate the frequency of the provided words
    word_frequencies = {word: word_counter[word] for word in word_keys}
    
    # Get the top_k most common words and their frequencies
    top_k_words = word_counter.most_common(top_k)
    
    # Create a DataFrame for plotting
    df = pd.DataFrame(list(top_k_words), columns=['word', 'frequency'])
    
    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(df['word'], df['frequency'])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top {} Most Common Words'.format(top_k))
    
    # Return the Axes object and the dictionary of top_k word frequencies
    return ax, word_frequencies