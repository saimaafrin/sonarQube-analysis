
import re
from nltk import word_tokenize
from collections import Counter

def task_func(input_str):
    # Remove special characters, punctuation marks, and spaces from the input string
    clean_str = re.sub(r'[^a-zA-Z\s]', '', input_str)

    # Tokenize the string into individual words
    words = word_tokenize(clean_str)

    # Count the frequency of each word
    word_freq = Counter(words)

    # Return the dictionary with the frequency of each word
    return word_freq