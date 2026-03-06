
import re
from collections import Counter

def task_func(text, top_n):
    # Remove URLs from the text
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    cleaned_text = re.sub(url_pattern, '', text)
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the N most common words
    most_common_words = word_counts.most_common(top_n)
    
    return most_common_words