
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

def task_func(mystrings, text):
    if not text:
        raise ValueError("Input text is empty")
    
    # Replace spaces with underscores and convert to lowercase
    modified_text = re.sub(r'\s+', '_', text).lower()
    
    # Split the text into words
    words = modified_text.split('_')
    
    # Count the frequency of each unique word
    word_counts = Counter(words)
    
    # Get the unique words and their frequencies
    unique_words = list(word_counts.keys())
    frequencies = list(word_counts.values())
    
    # Plot the frequency of each unique word
    fig, ax = plt.subplots()
    ax.bar(range(len(unique_words)), frequencies, tick_label=unique_words)
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Word Frequency')
    
    return ax