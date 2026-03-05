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
    dollar_words = [word for word in tokens if word.startswith('$')]

    # Remove "$" symbol from each dollar-prefixed word
    dollar_words = [word[1:] for word in dollar_words]

    # Count the frequency of each dollar-prefixed word
    word_counts = Counter(dollar_words)

    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the top five most frequent dollar-prefixed words and their counts
    return sorted_word_counts[:5]
text = "This is a sample text with some $dollar-prefixed words like $100 and $500."