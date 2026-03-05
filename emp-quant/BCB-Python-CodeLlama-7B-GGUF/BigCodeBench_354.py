
import collections
import matplotlib.pyplot as plt
import pandas as pd

# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def task_func(sentences_dict, word_keys):
    # Create a dictionary to store the word frequencies
    word_freqs = collections.defaultdict(int)

    # Iterate over the sentences in the dictionary
    for sentence in sentences_dict.values():
        # Tokenize the sentence
        tokens = sentence.split()

        # Iterate over the tokens
        for token in tokens:
            # Increment the frequency of the token
            word_freqs[token] += 1

    # Create a DataFrame to store the word frequencies
    word_freqs_df = pd.DataFrame(word_freqs.items(), columns=['word', 'frequency'])

    # Sort the DataFrame by frequency
    word_freqs_df.sort_values(by='frequency', inplace=True, ascending=False)

    # Create a bar chart of the word frequencies
    ax = word_freqs_df.plot.bar(x='word', y='frequency', rot=0)

    # Set the title and labels
    ax.set_title('Word Frequencies')
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')

    # Return the Axes object of the bar chart
    return ax

# Call the function
ax = task_func(sentences_dict, WORDS)

# Show the plot
plt.show()