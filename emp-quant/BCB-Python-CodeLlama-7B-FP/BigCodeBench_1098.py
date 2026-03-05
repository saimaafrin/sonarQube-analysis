import re
from collections import Counter
def task_func(text, top_n):
    """
    Count the N most common words in a text after removing URLs.
    Note that: Valid url is start with http or https
    The function should output with:
        list: A list of tuples where each tuple contains a word and its frequency.
    """
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

    # Tokenize the text
    tokens = re.split(r'\W+', text)

    # Create a Counter object
    counter = Counter(tokens)

    # Get the top N most common words
    top_words = counter.most_common(top_n)

    # Return a list of tuples
    return [(word, count) for word, count in top_words]
text = "This is a sample text with a URL: https://www.example.com/path/to/file.txt"
top_n = 3