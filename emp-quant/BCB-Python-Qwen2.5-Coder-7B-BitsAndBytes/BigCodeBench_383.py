
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
        n_gram = ' '.join(words[i:i+n])
        n_grams.append(n_gram)
    
    # Count the frequency of each n-gram
    n_gram_counts = Counter(n_grams)
    
    # Get the top k most common n-grams
    top_n_grams = n_gram_counts.most_common(top_k)
    
    # Create a DataFrame to store the results
    df = pd.DataFrame(top_n_grams, columns=['n-gram', 'count'])
    
    # Plot the results using seaborn
    sns.barplot(x='count', y='n-gram', data=df)
    plt.title(f'Top {top_k} {n}-grams')
    plt.xlabel('Frequency')
    plt.ylabel('n-gram')
    plt.show()