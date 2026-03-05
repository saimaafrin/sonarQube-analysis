import re
import string
from nltk.stem import PorterStemmer
from collections import Counter
STEMMER = PorterStemmer()
def task_func(content):
    # Remove punctuation and convert to lowercase
    content = re.sub(f"[{string.punctuation}]", "", content).lower()
    # Split the content into words
    words = content.split()
    # Stem all words except the last one
    stemmed_words = [STEMMER.stem(word) for word in words[:-1]]
    # Count the frequency of each stemmed word
    word_count = Counter(stemmed_words)
    return word_count