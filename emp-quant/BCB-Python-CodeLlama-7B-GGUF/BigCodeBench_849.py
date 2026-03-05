
import re
from nltk.corpus import stopwords
from collections import Counter

STOPWORDS = set(stopwords.words('english'))

def task_func(input_string):
    # Split the input string into individual lines
    lines = input_string.splitlines()

    # Remove stopwords from each line
    lines = [re.sub(r'\b(' + '|'.join(STOPWORDS) + r')\b', '', line) for line in lines]

    # Flatten the list of lines into a single string
    text = ' '.join(lines)

    # Tokenize the text into individual words
    words = text.split()

    # Count the frequency of each word
    word_freq = Counter(words)

    return word_freq