
import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt

def task_func(text, n, top_k):
    # Tokenize the text
    tokens = TextBlob(text).words

    # Create a counter for the n-grams
    counter = Counter(tokens)

    # Get the top K n-grams
    top_ngrams = counter.most_common(top_k)

    # Create a DataFrame for the n-grams
    df = pd.DataFrame(top_ngrams, columns=['n-gram', 'count'])

    # Plot the n-grams
    sns.barplot(x='n-gram', y='count', data=df)
    plt.show()