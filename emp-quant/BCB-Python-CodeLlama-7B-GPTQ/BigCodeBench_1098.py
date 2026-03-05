import re
from collections import Counter
def task_func(text, top_n):
    """
    Count the top_n most common words in a text after removing URLs.
    Valid URLs start with http or https.
    """
    # Remove URLs from the text
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

    # Tokenize the text
    tokens = re.split(r'\W+', text)

    # Create a Counter object
    counter = Counter(tokens)

    # Get the top_n most common words
    most_common = counter.most_common(top_n)

    # Return a list of tuples
    return most_common
text = "This is a sample text with http://www.example.com/url and https://www.example.com/url2"
top_n = 2