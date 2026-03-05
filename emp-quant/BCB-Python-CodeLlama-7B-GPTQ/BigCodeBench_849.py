import re
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))
def task_func(input_string):
    """
    Divide a multi-line string into individual lines, remove stopwords, and count the frequency of each word.
    The function should output with:
        dict: A dictionary with word frequencies where each key is a unique word and the value is its frequency.
    """
    # Split the input string into individual lines
    lines = input_string.splitlines()

    # Remove stopwords from each line
    lines = [re.sub(r'\b(?:{})\b'.format('|'.join(STOPWORDS)), '', line) for line in lines]

    # Split each line into individual words
    words = [line.split() for line in lines]

    # Flatten the list of words
    words = [word for sublist in words for word in sublist]

    # Count the frequency of each word
    word_freq = Counter(words)

    # Return the dictionary of word frequencies
    return word_freq
input_string = """
    This is a sample text with some stopwords.
    The stopwords are removed and the frequency of each word is counted.
"""