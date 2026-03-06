import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt
def task_func(text, n, top_k):
    """
    Visualize the uppermost K n-grams in a given text string.

    Parameters:
    text (str): The text string.
    n (int): The value of n for the n-grams.
    top_k (int): The number of top n-grams to visualize.

    Returns:
    None

    Requirements:
    - re
    - pandas
    - seaborn
    - textblob
    - matplotlib

    Example:
    >>> type(task_func('This is a sample text for testing.', 2, 5))
    <class 'matplotlib.axes._axes.Axes'>
    """
    # Create a list of n-grams
    ngrams = []
    for i in range(len(text) - n + 1):
        ngrams.append(text[i:i + n])

    # Create a dataframe with the n-grams and their counts
    df = pd.DataFrame(Counter(ngrams))
    df = df.sort_values(by=0, ascending=False)

    # Create a barplot of the top K n-grams
    ax = sns.barplot(x=0, y=1, data=df.head(top_k))
    ax.set_xlabel('n-gram')
    ax.set_ylabel('count')
    ax.set_title('Top {} n-grams'.format(top_k))

    return ax