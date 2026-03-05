
import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt

def task_func(text, n, top_k):
    # Split the text into words
    words = text.split()
    
    # Generate n-grams
    n_grams = []
    for i in range(len(words) - n + 1):
        n_grams.append(' '.join(words[i:i+n]))
    
    # Count the frequency of each n-gram
    n_gram_counts = Counter(n_grams)
    
    # Get the top K n-grams
    top_n_grams = n_gram_counts.most_common(top_k)
    
    # Create a DataFrame for visualization
    df = pd.DataFrame(top_n_grams, columns=['n-gram', 'frequency'])
    
    # Plot the top K n-grams
    plt.figure(figsize=(10, 6))
    sns.barplot(x='frequency', y='n-gram', data=df)
    plt.title(f'Top {top_k} {n}-grams')
    plt.xlabel('Frequency')
    plt.ylabel('n-gram')
    plt.show()
    
    return None