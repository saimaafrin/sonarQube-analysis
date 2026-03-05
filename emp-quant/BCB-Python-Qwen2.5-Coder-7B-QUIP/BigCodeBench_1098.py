
import re
from collections import Counter

def task_func(text, top_n):
    # Remove URLs from the text
    text = re.sub(r'http[s]?://\S+', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the top N most common words
    top_words = word_counts.most_common(top_n)
    
    return top_words