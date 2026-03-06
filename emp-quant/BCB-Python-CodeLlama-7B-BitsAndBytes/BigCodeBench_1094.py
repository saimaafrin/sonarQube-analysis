
from nltk.tokenize import RegexpTokenizer
from collections import Counter

def task_func(text):
    # Tokenize the text using NLTK's RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)

    # Filter out tokens that are only "$" symbols
    filtered_tokens = [token for token in tokens if token != '$' and token[0] == '$']

    # Create a Counter object to count the frequency of each dollar-prefixed word
    counter = Counter(filtered_tokens)

    # Sort the counter by frequency and return the top 5 most frequent words
    top_5 = counter.most_common(5)

    return top_5