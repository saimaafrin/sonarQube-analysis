
import re
from collections import Counter

def task_func(text, top_n):
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

    # Tokenize the text
    tokens = text.split()

    # Count the top N most common words
    counter = Counter(tokens)
    most_common = counter.most_common(top_n)

    # Return a list of tuples with the words and their frequencies
    return [(word, freq) for word, freq in most_common]