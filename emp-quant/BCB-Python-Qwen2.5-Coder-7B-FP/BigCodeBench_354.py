import collections
import matplotlib.pyplot as plt
import pandas as pd
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
def task_func(sentences_dict, word_keys):
    # Initialize a dictionary to store word counts
    word_counts = {word: 0 for word in WORDS}
    
    # Iterate over the sentences in the dictionary
    for sentences in sentences_dict.values():
        for sentence in sentences:
            # Split the sentence into words and count occurrences
            for word in sentence.split():
                if word in word_counts:
                    word_counts[word] += 1
    
    # Filter the word counts based on the provided word keys
    filtered_word_counts = {word: count for word, count in word_counts.items() if word in word_keys}
    
    # Create a DataFrame from the filtered word counts
    df = pd.DataFrame(list(filtered_word_counts.items()), columns=['Word', 'Count'])
    
    # Create a bar chart using matplotlib
    ax = df.plot(kind='bar', x='Word', y='Count', legend=False)
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    ax.set_title('Word Frequency in Sentences')
    
    return ax