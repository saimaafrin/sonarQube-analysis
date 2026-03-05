
import collections
import matplotlib.pyplot as plt
import pandas as pd

# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def task_func(sentences_dict, word_keys):
    # Initialize a dictionary to store word counts
    word_counts = collections.defaultdict(int)
    
    # Iterate over each sentence in the dictionary
    for key, sentences in sentences_dict.items():
        # Split each sentence into words and count occurrences
        for sentence in sentences:
            words = sentence.split()
            for word in words:
                if word in word_keys:
                    word_counts[word] += 1
    
    # Create a DataFrame from the word counts
    df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count'])
    
    # Sort the DataFrame by count in descending order
    df = df.sort_values(by='Count', ascending=False)
    
    # Create a bar chart
    ax = df.plot(kind='bar', x='Word', y='Count', legend=False)
    
    # Set the title and labels
    ax.set_title('Word Frequencies')
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object
    return ax