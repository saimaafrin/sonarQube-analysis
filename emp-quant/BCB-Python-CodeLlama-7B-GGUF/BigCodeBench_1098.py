
import re
from collections import Counter

def task_func(text, top_n):
    # Remove URLs from the text
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

    # Split the text into individual words
    words = text.split()

    # Create a Counter object to count the frequency of each word
    counter = Counter(words)

    # Sort the Counter object by frequency and return the top N most common words
    return counter.most_common(top_n)