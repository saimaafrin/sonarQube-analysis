import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt
def task_func(text, n, top_k):
    # Split the text into words
    words = text.split()
    
    # Generate n-grams
    ngrams = [tuple(words[i:i+n]) for i in range(len(words) - n + 1)]
    
    # Count the frequency of each n-gram
    ngram_counts = Counter(ngrams)
    
    # Get the top K n-grams
    top_ngrams = ngram_counts.most_common(top_k)
    
    # Create a DataFrame for visualization
    df = pd.DataFrame(top_ngrams, columns=['n-gram', 'count'])
    
    # Plot the top K n-grams
    plt.figure(figsize=(10, 6))
    sns.barplot(x='count', y='n-gram', data=df)
    plt.title(f'Top {top_k} {n}-grams')
    plt.xlabel('Frequency')
    plt.ylabel('n-gram')
    plt.show()
    
    # Return None as per the requirement
    return None