import re
import string
from nltk.stem import PorterStemmer
from collections import Counter
STEMMER = PorterStemmer()
def task_func(content):
    """
    Stem every word in a sentence, except the last, and count the frequency of each stem.
    :param content: The sentence to be stemmed.
    :return: A dictionary with stemmed words as keys and their frequency as values.
    """
    words = re.split(r'\W+', content)
    stemmed_words = [STEMMER.stem(word) for word in words[:-1]]
    return Counter(stemmed_words)