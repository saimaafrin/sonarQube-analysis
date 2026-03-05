import collections
import matplotlib.pyplot as plt
import pandas as pd
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
def task_func(sentences_dict, word_keys):
    """
    Calculate the occurrence of certain words in a collection of sentences and return a bar chart.
    """
    # Create a dictionary to store the word frequencies
    word_freq = collections.defaultdict(int)

    # Iterate over the sentences in the dictionary
    for sentence in sentences_dict.values():
        # Tokenize the sentence
        tokens = sentence.split()

        # Iterate over the tokens in the sentence
        for token in tokens:
            # Check if the token is in the list of words to count
            if token in word_keys:
                # Increment the frequency of the token
                word_freq[token] += 1

    # Create a Pandas DataFrame from the word frequencies
    df = pd.DataFrame(word_freq.items(), columns=['word', 'frequency'])

    # Sort the DataFrame by frequency
    df = df.sort_values(by='frequency', ascending=False)

    # Create a bar chart of the word frequencies
    ax = df.plot(kind='bar', x='word', y='frequency', rot=0)

    # Return the Axes object of the bar chart
    return ax
sentences_dict = {
    'sentence1': 'The quick brown fox jumps over the lazy dog.',
    'sentence2': 'The quick brown fox jumps over the lazy dog.',
    'sentence3': 'The quick brown fox jumps over the lazy dog.',
    'sentence4': 'The quick brown fox jumps over the lazy dog.',
    'sentence5': 'The quick brown fox jumps over the lazy dog.',
}