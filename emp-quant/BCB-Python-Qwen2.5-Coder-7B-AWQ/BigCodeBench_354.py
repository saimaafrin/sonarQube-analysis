import collections
import matplotlib.pyplot as plt
import pandas as pd
def task_func(sentences_dict, word_keys):
    # Initialize a dictionary to store word frequencies
    word_freq = {word: 0 for word in word_keys}
    
    # Iterate over each sentence in the dictionary
    for sentences in sentences_dict.values():
        # Split the sentence into words and count the frequency of each word
        for word in sentences.split():
            if word in word_freq:
                word_freq[word] += 1
    
    # Create a DataFrame from the word frequencies
    df = pd.DataFrame(list(word_freq.items()), columns=['Word', 'Frequency'])
    
    # Create a bar chart using matplotlib
    ax = df.plot(kind='bar', x='Word', y='Frequency', legend=False)
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    ax.set_title('Word Frequencies')
    
    return ax