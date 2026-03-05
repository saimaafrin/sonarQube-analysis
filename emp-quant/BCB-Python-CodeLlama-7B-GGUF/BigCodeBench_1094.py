
from nltk.tokenize import RegexpTokenizer
from collections import Counter

def task_func(text):
    # Tokenize the text using a regular expression
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)

    # Filter out tokens that do not start with "$"
    filtered_tokens = [token for token in tokens if token.startswith('$')]

    # Create a Counter object to count the frequency of each token
    counter = Counter(filtered_tokens)

    # Sort the counter by frequency and return the top 5 most frequent tokens
    top_tokens = counter.most_common(5)

    return top_tokens