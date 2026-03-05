import collections
import matplotlib.pyplot as plt
import pandas as pd
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
def task_func(sentences_dict, word_keys):
    """
    Calculate the occurrence of certain words in a collection of sentences and return a bar chart.
    """
    # Create a dictionary to store the word frequencies
    word_freq = collections.Counter()

    # Iterate over the sentences in the dictionary
    for sentence in sentences_dict:
        # Tokenize the sentence into individual words
        words = sentence.split()

        # Iterate over the words in the sentence
        for word in words:
            # If the word is in the list of target words, increment its frequency
            if word in word_keys:
                word_freq[word] += 1

    # Create a DataFrame from the word frequencies
    word_freq_df = pd.DataFrame.from_dict(word_freq, orient='index')

    # Sort the DataFrame by frequency
    word_freq_df.sort_values(by='value', inplace=True)

    # Create a bar chart of the word frequencies
    ax = word_freq_df.plot(kind='bar', rot=0, figsize=(10, 6))

    # Set the x-axis labels
    ax.set_xticklabels(word_freq_df.index, rotation=90)

    # Set the y-axis label
    ax.set_ylabel('Frequency')

    # Return the Axes object of the bar chart
    return ax
sentences_dict = {
    'Sentence 1': 'The quick brown fox jumps over the lazy dog.',
    'Sentence 2': 'The quick brown fox jumps over the lazy dog.',
    'Sentence 3': 'The quick brown fox jumps over the lazy dog.',
    'Sentence 4': 'The quick brown fox jumps over the lazy dog.',
    'Sentence 5': 'The quick brown fox jumps over the lazy dog.'
}