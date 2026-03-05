import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter
def task_func(mystrings, text):
    if not text:
        raise ValueError("Input text is empty")
    
    # Convert text to lowercase and replace spaces with underscores
    modified_text = re.sub(r'\s+', '_', text.lower())
    
    # Split the modified text into words
    words = modified_text.split('_')
    
    # Count the frequency of each unique word
    word_counts = Counter(words)
    
    # Get the unique words and their frequencies
    unique_words = list(word_counts.keys())
    frequencies = list(word_counts.values())
    
    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(unique_words, frequencies)
    
    # Set the title and labels
    ax.set_title('Word Frequency')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    
    return ax