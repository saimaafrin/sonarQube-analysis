from nltk.tokenize import RegexpTokenizer
from collections import Counter
def task_func(text):
    """
    Identifies and counts words in a given text that start with the "$" symbol.
    It returns the five most frequent dollar-prefixed words along with their counts.
    Words solely consisting of "$" symbols without any following alphanumeric characters are ignored in the frequency count.
    The function should output with:
        list of tuples: Each tuple contains a dollar-prefixed word (excluding the "$" symbol) and its frequency,
        ordered by most to least common.
    """
    # Tokenize the text using NLTK's RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)

    # Create a list of tuples containing the dollar-prefixed words and their frequencies
    dollar_words = []
    for token in tokens:
        if token.startswith('$') and token != '$':
            dollar_words.append((token[1:], 1))

    # Create a Counter object to count the frequencies of the dollar-prefixed words
    counter = Counter(dollar_words)

    # Sort the counter by frequency and return the top 5 most frequent dollar-prefixed words
    return counter.most_common(5)
text = "This is a test text with $dollar, $sign, and $100."