
import collections
import matplotlib.pyplot as plt
import pandas as pd

# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def task_func(sentences_dict, word_keys):
    # Initialize a dictionary to store word counts
    word_counts = {word: 0 for word in WORDS}
    
    # Iterate over each sentence in the dictionary
    for key, sentences in sentences_dict.items():
        if key in word_keys:
            # Split each sentence into words and count occurrences
            for sentence in sentences:
                words = sentence.split()
                for word in words:
                    if word.lower() in word_counts:
                        word_counts[word.lower()] += 1
    
    # Create a DataFrame from the word counts
    df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count'])
    
    # Plotting the bar chart
    ax = df.plot(kind='bar', x='Word', y='Count', legend=False)
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Word Frequency in Sentences')
    
    return ax