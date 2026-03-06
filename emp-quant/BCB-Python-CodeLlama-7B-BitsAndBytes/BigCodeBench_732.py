
import re
import string
from nltk.stem import PorterStemmer
from collections import Counter

STEMMER = PorterStemmer()

def task_func(content):
    # Tokenize the input text
    tokens = re.split(r'\W+', content)

    # Stem every word except the last
    stemmed_tokens = [STEMMER.stem(token) for token in tokens[:-1]]

    # Count the frequency of each stem
    stem_counts = Counter(stemmed_tokens)

    # Return the stemmed words and their frequencies as a dictionary
    return dict(stem_counts)