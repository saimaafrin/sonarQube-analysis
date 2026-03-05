
import re
import string
from nltk.stem import PorterStemmer
from collections import Counter

STEMMER = PorterStemmer()

def task_func(content):
    # Split the content into words
    words = content.split()
    
    # Stem all words except the last one
    stemmed_words = [STEMMER.stem(word) for word in words[:-1]]
    
    # Count the frequency of each stemmed word
    word_count = Counter(stemmed_words)
    
    # Return the result as a dictionary
    return dict(word_count)