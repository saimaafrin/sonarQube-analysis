
import re
import string
from nltk.stem import PorterStemmer
from collections import Counter

STEMMER = PorterStemmer()

def task_func(content):
    # Tokenize the input text
    tokens = re.split(r'\W+', content)

    # Stem each word in the token list
    stemmed_tokens = [STEMMER.stem(token) for token in tokens]

    # Create a dictionary with stemmed words as keys and their frequency as values
    stem_counts = Counter(stemmed_tokens)

    return stem_counts