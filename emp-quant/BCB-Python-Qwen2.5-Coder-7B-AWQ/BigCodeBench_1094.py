from nltk.tokenize import RegexpTokenizer
from collections import Counter
def task_func(text):
    # Initialize a tokenizer to split text into words
    tokenizer = RegexpTokenizer(r'\b\w+\b')
    # Tokenize the input text
    words = tokenizer.tokenize(text)
    # Filter words that start with '$' and exclude those with only '$'
    dollar_words = [word[1:] for word in words if word.startswith('$') and len(word) > 1]
    # Count the frequency of each dollar-prefixed word
    word_counts = Counter(dollar_words)
    # Get the five most common words
    most_common_words = word_counts.most_common(5)
    return most_common_words