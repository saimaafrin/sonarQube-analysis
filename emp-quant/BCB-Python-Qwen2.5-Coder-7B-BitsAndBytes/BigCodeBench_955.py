
import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

def task_func(mystrings, text):
    if not text.strip():
        raise ValueError("Input text cannot be empty.")
    
    # Convert text to lowercase and replace spaces with underscores
    modified_text = re.sub(r'\s+', '_', text.lower())
    
    # Split the modified text into words
    words = modified_text.split('_')
    
    # Filter out any empty strings that may result from consecutive spaces
    words = [word for word in words if word]
    
    # Count the frequency of each unique word
    word_counts = Counter(words)
    
    # Extract words and their frequencies
    words_list = list(word_counts.keys())
    counts_list = list(word_counts.values())
    
    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(words_list, counts_list)
    
    # Set labels and title
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Word Frequency Plot')
    
    return ax