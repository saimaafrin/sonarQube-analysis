
import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt

def task_func(text, n, top_k):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Extract n-grams
    ngrams = blob.noun_phrases
    
    # Count the frequency of each n-gram
    ngram_counts = Counter(ngrams)
    
    # Get the top K n-grams
    top_ngrams = ngram_counts.most_common(top_k)
    
    # Create a DataFrame
    df = pd.DataFrame(top_ngrams, columns=['N-gram', 'Frequency'])
    
    # Plot the top K n-grams
    sns.barplot(x='N-gram', y='Frequency', data=df)
    plt.xticks(rotation=45)
    plt.show()
    
    # Return None
    return None