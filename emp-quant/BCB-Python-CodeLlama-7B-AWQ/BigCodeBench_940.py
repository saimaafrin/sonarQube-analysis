import re
from nltk import word_tokenize
from collections import Counter
def task_func(input_str):
    """
    Remove all special characters, punctuation marks and spaces from a string called "input_str" using regex and then count the frequency of each word.
    """
    # Remove special characters, punctuation marks and spaces from input_str
    input_str = re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
    # Tokenize the input_str into individual words
    words = word_tokenize(input_str)
    # Create a dictionary with the frequency of each word
    word_freq = Counter(words)
    return word_freq
input_str = "Hello, World! How are you? I'm fine, thank you."