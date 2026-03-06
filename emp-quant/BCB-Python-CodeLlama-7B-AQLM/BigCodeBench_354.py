import collections
import matplotlib.pyplot as plt
import pandas as pd
def task_func(sentences_dict, word_keys):
    """
    Calculate the occurrence of certain words in a collection of sentences and return a bar chart.

    Parameters:
    sentences_dict (dict): The dictionary containing sentences.
    word_keys (list): The list of words.

    Returns:
    - matplotlib.axes._axes.Axes: Axes object of the bar chart displaying the frequencies.

    Requirements:
    - collections
    - matplotlib.pyplot
    - pandas

    Example:
    >>> sentences_dict = {'Sentence1': 'the quick brown fox', 'Sentence2': 'jumps over the lazy dog', 'Sentence3': 'the dog is brown'}
    >>> word_keys = ['the', 'dog']
    >>> type(task_func(sentences_dict, word_keys))
    <class 'matplotlib.axes._axes.Axes'>
    """
    # Create a dataframe with the word counts
    df = pd.DataFrame(columns=['Word', 'Count'])
    for sentence in sentences_dict.values():
        for word in sentence.split():
            if word in word_keys:
                df = df.append({'Word': word, 'Count': df[df['Word'] == word]['Count'].sum() + 1}, ignore_index=True)
    # Sort the dataframe by the word counts
    df = df.sort_values(by='Count', ascending=False)
    # Create a bar chart
    ax = df.plot.bar(x='Word', y='Count', rot=0, figsize=(10, 5))
    # Set the x-axis labels
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    # Set the y-axis labels
    ax.set_ylabel('Count')
    # Set the x-axis labels
    ax.set_xlabel('Word')
    # Return the axes object
    return ax