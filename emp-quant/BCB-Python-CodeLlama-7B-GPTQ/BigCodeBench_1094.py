from nltk.tokenize import RegexpTokenizer
from collections import Counter
def task_func(text):
    """
    Identifies and counts words in a given text that start with the "$" symbol.
    It returns the five most frequent dollar-prefixed words along with their counts.
    Words solely consisting of "$" symbols without any following alphanumeric characters are ignored in the frequency count.
    """
    # Tokenize the text into individual words
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)

    # Filter out words that do not start with "$"
    filtered_tokens = [token for token in tokens if token.startswith('$')]

    # Create a Counter object to count the frequency of each word
    counter = Counter(filtered_tokens)

    # Sort the Counter object by frequency and return the top five most frequent words
    top_five = counter.most_common(5)

    # Return a list of tuples containing the word and its frequency
    return [(word, count) for word, count in top_five]
text = "This is a sample text with some $dollar-prefixed words like $100 and $500."