import re
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))
def task_func(input_string):
    """
    Divide a multi-line string into individual lines, remove stopwords, and count the frequency of each word.
    :param input_string: A multi-line string
    :return: A dictionary with word frequencies where each key is a unique word and the value is its frequency
    """
    # Split the input string into individual lines
    lines = input_string.splitlines()

    # Remove stopwords from each line
    lines = [re.sub(r'\b(' + r'|'.join(STOPWORDS) + r')\b', '', line) for line in lines]

    # Flatten the list of lines into a single string
    text = ' '.join(lines)

    # Tokenize the text into individual words
    words = text.split()

    # Count the frequency of each word
    word_freq = Counter(words)

    return word_freq
input_string = """
This is a sample text with some stopwords.
It has multiple lines and some punctuation.
"""