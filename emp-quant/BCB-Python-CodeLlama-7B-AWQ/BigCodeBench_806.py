import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))
def task_func(text, n=2):
    """
    Remove duplicate and stopwords from a string "text." Then, generate a count of n-grams (default is bigrams) in the text.
    The function should output with:
        dict: The count of the n-grams in the text.
    """
    # Remove duplicate and stopwords
    text = re.sub(r'\b(' + r'|'.join(STOPWORDS) + r')\b', '', text)
    text = re.sub(r'\b(' + r'|'.join(STOPWORDS) + r')\b', '', text)
    # Generate n-grams
    ngrams = Counter()
    for i in range(len(text) - n + 1):
        ngrams[text[i:i+n]] += 1
    return ngrams