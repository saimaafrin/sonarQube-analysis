import re
from nltk import word_tokenize
from collections import Counter
def task_func(input_str):
    # Remove all special characters, punctuation marks, and spaces from the input string
    clean_str = re.sub(r'[^a-zA-Z0-9\s]', '', input_str)

    # Tokenize the cleaned string into individual words
    words = word_tokenize(clean_str)

    # Count the frequency of each word
    word_freq = Counter(words)

    # Return the dictionary of word frequencies
    return word_freq
input_str = "Hello, World! How are you?"