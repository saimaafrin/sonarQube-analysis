
import collections
import matplotlib.pyplot as plt
import pandas as pd

# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def task_func(sentences_dict, word_keys):
    # Create a dictionary to store the word frequencies
    word_freq = collections.Counter()

    # Iterate over the sentences in the dictionary
    for sentence in sentences_dict:
        # Tokenize the sentence
        tokens = sentence.split()

        # Iterate over the tokens in the sentence
        for token in tokens:
            # Check if the token is in the list of words to count
            if token in word_keys:
                # Increment the frequency of the token
                word_freq[token] += 1

    # Create a DataFrame to store the word frequencies
    df = pd.DataFrame(word_freq.items(), columns=['word', 'frequency'])

    # Sort the DataFrame by frequency
    df.sort_values(by='frequency', inplace=True, ascending=False)

    # Create a bar chart of the word frequencies
    ax = df.plot(kind='bar', x='word', y='frequency', rot=0)

    # Set the title and labels
    ax.set_title('Word Frequencies')
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')

    # Return the Axes object
    return ax

# Get the word frequencies
ax = task_func(sentences_dict, WORDS)

# Display the bar chart
plt.show()