
import collections
import matplotlib.pyplot as plt
import pandas as pd

# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def task_func(sentences_dict, word_keys):
    # Initialize a dictionary to store word counts
    word_counts = {word: 0 for word in word_keys}
    
    # Iterate over each sentence in the dictionary
    for sentences in sentences_dict.values():
        for sentence in sentences:
            # Split the sentence into words and count occurrences
            words = sentence.split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
    
    # Create a DataFrame from the word counts
    df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count'])
    
    # Create a bar chart
    ax = df.plot(kind='bar', x='Word', y='Count', legend=False)
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    ax.set_title('Word Frequency in Sentences')
    
    return ax