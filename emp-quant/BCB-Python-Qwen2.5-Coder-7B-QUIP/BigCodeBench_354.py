
import collections
import matplotlib.pyplot as plt
import pandas as pd
# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def task_func(sentences_dict, word_keys):
    # Initialize a dictionary to store word counts
    word_counts = collections.defaultdict(int)

    # Iterate over the sentences and count the occurrences of each word
    for sentence in sentences_dict.values():
        words = sentence.split()
        for word in words:
            if word in word_keys:
                word_counts[word] += 1

    # Convert the dictionary to a DataFrame for easier plotting
    df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count'])

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(df['Word'], df['Count'], color='blue')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Word Frequency in Sentences')
    ax.set_xticklabels(df['Word'], rotation=45)

    # Return the Axes object
    return ax