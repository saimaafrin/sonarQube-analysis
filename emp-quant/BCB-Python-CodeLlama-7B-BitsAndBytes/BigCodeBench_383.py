
import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt

def task_func(text, n, top_k):
    # Create a TextBlob object from the input text
    blob = TextBlob(text)

    # Get the n-grams from the TextBlob object
    ngrams = blob.ngrams(n)

    # Create a Counter object from the n-grams
    counter = Counter(ngrams)

    # Get the top K n-grams from the Counter object
    top_ngrams = counter.most_common(top_k)

    # Create a DataFrame from the top n-grams
    df = pd.DataFrame(top_ngrams, columns=['ngram', 'count'])

    # Plot the n-grams using Seaborn
    sns.barplot(x='ngram', y='count', data=df)

    # Show the plot
    plt.show()