
import re
import string
from nltk.stem import PorterStemmer
from collections import Counter
STEMMER = PorterStemmer()
def task_func(content):
    words = re.findall(r'\w+', content)
    stemmed_words = [STEMMER.stem(word) for word in words]
    return Counter(stemmed_words)