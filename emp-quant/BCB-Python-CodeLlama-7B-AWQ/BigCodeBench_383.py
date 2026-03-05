import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt
def task_func(text, n, top_k):
    """
    Visualize the uppermost K n-grams in a given text string.
    """
    # Tokenize the text
    tokens = TextBlob(text).words

    # Count the n-grams
    ngrams = Counter(tokens).most_common(n)

    # Create a DataFrame with the n-grams and their counts
    df = pd.DataFrame(ngrams, columns=['ngram', 'count'])

    # Sort the DataFrame by count
    df.sort_values(by='count', ascending=False, inplace=True)

    # Plot the top K n-grams
    sns.barplot(x='ngram', y='count', data=df.head(top_k))
    plt.show()
text = "This is a sample text with some n-grams."
n = 2
top_k = 5