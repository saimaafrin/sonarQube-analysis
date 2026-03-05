
import re
from collections import Counter
import matplotlib.pyplot as plt

def task_func(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation using regex
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the top 10 most common words
    top_10_words = word_counts.most_common(10)
    
    # Create a bar chart for the top 10 words
    fig, ax = plt.subplots()
    ax.bar([word for word, count in top_10_words], [count for word, count in top_10_words])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Common Words')
    
    return top_10_words, ax