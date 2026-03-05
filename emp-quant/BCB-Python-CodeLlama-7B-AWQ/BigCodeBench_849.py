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

    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    # Iterate over each line
    for line in lines:
        # Tokenize the line into individual words
        words = line.split()

        # Iterate over each word
        for word in words:
            # Remove stopwords
            if word in STOPWORDS:
                continue

            # Increment the frequency of the word
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1

    return word_freq
input_string = """
This is a sample text with some stopwords.
It has multiple lines and some punctuation.
"""