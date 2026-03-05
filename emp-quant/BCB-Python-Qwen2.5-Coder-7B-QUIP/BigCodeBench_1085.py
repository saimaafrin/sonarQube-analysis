
import re
from collections import Counter
import matplotlib.pyplot as plt

def task_func(text):
    # Lowercase the text
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the top 10 most common words
    top_10 = word_counts.most_common(10)
    
    # Plot the top 10 most common words
    fig, ax = plt.subplots()
    ax.bar([word for word, count in top_10], [count for word, count in top_10])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Common Words')
    
    return top_10, ax